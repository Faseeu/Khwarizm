"""
tools/project_runner_tool.py

ProjectRunnerTool
=================
Manages and executes a full multi-file Python project with pip package support.

Strategy
--------
- Each project lives in its own directory under a configurable base path.
- Packages are installed into a project-local virtual environment (one venv
  per project, reused across runs — no rebuild unless explicitly reset).
- Execution uses subprocess with:
    • shell=False  (no injection surface)
    • an explicit argument list
    • a timeout
    • cwd set to the project directory
    • a clean, minimal environment (no host secrets leaked)
    • stdout/stderr captured and returned
- File writes are validated before touching disk.
- The agent interacts through a structured tool interface; humans see a clear
  result dict with every detail they need to understand what happened.

When to use this tool
---------------------
Use when:
- The task requires multiple Python files (modules, packages, configs).
- Third-party packages (pandas, requests, etc.) need to be installed.
- The project needs to persist between agent turns (files survive the call).

For single-file stdlib-only scripts use PythonRunnerTool instead — it is
faster and requires no venv setup.
"""

from tools.basetool import BaseTool

import json
import os
import shutil
import subprocess
import sys
import textwrap
import time
import venv
from pathlib import Path


# ── Tunables ──────────────────────────────────────────────────────────────────

DEFAULT_BASE_DIR    = ".agent_projects"   # relative to CWD; override in __init__
RUN_TIMEOUT_SECONDS = 60                  # per-execution wall-clock limit
PIP_TIMEOUT_SECONDS = 120                 # per-install wall-clock limit
MAX_OUTPUT_CHARS    = 100_000             # truncate beyond this
MAX_FILE_SIZE_BYTES = 1_000_000           # 1 MB per file write limit
MAX_FILES_PER_PROJECT = 100


# ── Allowed actions ───────────────────────────────────────────────────────────

ACTIONS = {
    "write_file":      "Create or overwrite a file in the project.",
    "read_file":       "Read a file from the project.",
    "list_files":      "List all files in the project.",
    "delete_file":     "Delete a file from the project.",
    "install_package": "Install a pip package into the project venv.",
    "list_packages":   "List packages installed in the project venv.",
    "run":             "Execute a Python file inside the project venv.",
    "run_snippet":     "Run an ad-hoc Python snippet inside the project venv.",
    "reset":           "Delete the entire project directory and start fresh.",
    "status":          "Return project metadata (files, packages, venv path).",
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _clean_env() -> dict:
    """
    Return a minimal environment for subprocesses.
    Strips secrets (API keys, tokens) while keeping PATH and locale.
    """
    keep = {"PATH", "HOME", "USER", "LANG", "LC_ALL", "LC_CTYPE",
            "TERM", "TMPDIR", "TMP", "TEMP", "SYSTEMROOT", "USERPROFILE"}
    return {k: v for k, v in os.environ.items() if k in keep}


def _truncate(text: str, limit: int = MAX_OUTPUT_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n[...output truncated at {limit} chars]"


def _safe_relpath(base: Path, target: str) -> Path:
    """
    Resolve *target* relative to *base* and verify it stays inside *base*.
    Raises ValueError on traversal attempts.
    """
    resolved = (base / target).resolve()
    try:
        resolved.relative_to(base.resolve())
    except ValueError:
        raise ValueError(
            f"Path traversal blocked: {target!r} escapes project root."
        )
    return resolved


# ── Tool class ────────────────────────────────────────────────────────────────

class ProjectRunnerTool(BaseTool):
    """
    Full project execution environment for the agent.

    One tool, many actions. The agent picks the action it needs and
    supplies the matching parameters. Every action returns a structured
    dict so the agent can reason about the result and the human can read
    the log without digging into internals.

    Project layout on disk
    ----------------------
    <base_dir>/
      <project_id>/
        files/          ← all user/agent-written source files live here
          main.py
          utils/
            helpers.py
          ...
        venv/           ← project-local virtual environment (created on first use)
        run.log         ← append-only log of every run (not returned to agent)
    """

    def __init__(self, base_dir: str = DEFAULT_BASE_DIR):
        self.base_dir = Path(base_dir).resolve()
        self.base_dir.mkdir(parents=True, exist_ok=True)

        self.name = "project_runner"
        self.description = (
            "Manage and execute a full multi-file Python project with pip package support. "
            "Actions: write_file, read_file, list_files, delete_file, "
            "install_package, list_packages, run, run_snippet, reset, status. "
            "Each project is isolated in its own directory with its own venv."
        )
        self.parameters = {
            "project_id": (
                "Short identifier for the project, e.g. 'web_scraper'. "
                "Alphanumeric, hyphens, underscores. Max 40 chars. "
                "The same project_id re-uses the same directory and venv across calls."
            ),
            "action": (
                "One of: " + ", ".join(ACTIONS.keys()) + ". "
                "See tool description for what each action does."
            ),
            "filename": (
                "[write_file, read_file, delete_file, run] "
                "Path relative to the project root, e.g. 'main.py' or 'utils/helpers.py'."
            ),
            "content": (
                "[write_file] Full content of the file as a string."
            ),
            "package": (
                "[install_package] PyPI package name, optionally with version, "
                "e.g. 'requests' or 'pandas==2.2.0'."
            ),
            "code": (
                "[run_snippet] A Python code snippet to execute inside the project venv. "
                "The project files directory is on sys.path."
            ),
            "entry_args": (
                "[run] Optional list of command-line arguments to pass to the script, "
                "e.g. ['--input', 'data.csv']. Defaults to []."
            ),
        }

    # ── Dispatch ──────────────────────────────────────────────────────────────

    def run(self, parameters: dict) -> dict:
        """
        Route to the appropriate action handler.

        Always returns a dict with at least:
            success : bool
            action  : str
            project : str
            message : str   — human-readable summary
            error   : str | None
        """
        project_id = parameters.get("project_id", "").strip()
        action     = parameters.get("action", "").strip()

        # ── Validate project_id ───────────────────────────────────────
        pid_err = self._validate_project_id(project_id)
        if pid_err:
            return self._err(project_id, action, pid_err)

        # ── Validate action ───────────────────────────────────────────
        if action not in ACTIONS:
            return self._err(project_id, action,
                f"Unknown action {action!r}. Valid actions: {', '.join(ACTIONS)}")

        project_dir = self.base_dir / project_id
        files_dir   = project_dir / "files"
        venv_dir    = project_dir / "venv"

        # ── Ensure project directory exists (except for reset) ────────
        if action != "reset":
            files_dir.mkdir(parents=True, exist_ok=True)

        # ── Route ─────────────────────────────────────────────────────
        try:
            if action == "write_file":
                return self._write_file(project_id, files_dir, parameters)
            elif action == "read_file":
                return self._read_file(project_id, files_dir, parameters)
            elif action == "list_files":
                return self._list_files(project_id, files_dir)
            elif action == "delete_file":
                return self._delete_file(project_id, files_dir, parameters)
            elif action == "install_package":
                return self._install_package(project_id, venv_dir, parameters)
            elif action == "list_packages":
                return self._list_packages(project_id, venv_dir)
            elif action == "run":
                return self._run_file(project_id, files_dir, venv_dir, parameters)
            elif action == "run_snippet":
                return self._run_snippet(project_id, files_dir, venv_dir, parameters)
            elif action == "reset":
                return self._reset(project_id, project_dir)
            elif action == "status":
                return self._status(project_id, project_dir, files_dir, venv_dir)
        except Exception as exc:
            import traceback
            return self._err(project_id, action,
                f"Unexpected error: {exc}\n{traceback.format_exc()}")

    # ── Action: write_file ────────────────────────────────────────────────────

    def _write_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "").strip()
        content  = params.get("content", "")

        if not filename:
            return self._err(pid, "write_file", "'filename' is required.")
        if not isinstance(content, str):
            return self._err(pid, "write_file", "'content' must be a string.")
        if len(content.encode()) > MAX_FILE_SIZE_BYTES:
            return self._err(pid, "write_file",
                f"File exceeds size limit ({MAX_FILE_SIZE_BYTES // 1000} KB).")

        # Count existing files
        existing = list(files_dir.rglob("*"))
        if len(existing) >= MAX_FILES_PER_PROJECT:
            return self._err(pid, "write_file",
                f"Project file limit ({MAX_FILES_PER_PROJECT}) reached.")

        try:
            target = _safe_relpath(files_dir, filename)
        except ValueError as e:
            return self._err(pid, "write_file", str(e))

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

        return {
            "success": True, "action": "write_file", "project": pid,
            "filename": filename,
            "bytes_written": len(content.encode()),
            "path": str(target),
            "message": f"Wrote {filename} ({len(content.encode())} bytes).",
            "error": None,
        }

    # ── Action: read_file ─────────────────────────────────────────────────────

    def _read_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "").strip()
        if not filename:
            return self._err(pid, "read_file", "'filename' is required.")
        try:
            target = _safe_relpath(files_dir, filename)
        except ValueError as e:
            return self._err(pid, "read_file", str(e))
        if not target.exists():
            return self._err(pid, "read_file", f"File not found: {filename!r}")
        content = target.read_text(encoding="utf-8")
        return {
            "success": True, "action": "read_file", "project": pid,
            "filename": filename,
            "content": content,
            "bytes": len(content.encode()),
            "message": f"Read {filename} ({len(content.encode())} bytes).",
            "error": None,
        }

    # ── Action: list_files ────────────────────────────────────────────────────

    def _list_files(self, pid: str, files_dir: Path) -> dict:
        if not files_dir.exists():
            return {
                "success": True, "action": "list_files", "project": pid,
                "files": [], "message": "Project is empty.", "error": None,
            }
        files = []
        for p in sorted(files_dir.rglob("*")):
            if p.is_file():
                rel = str(p.relative_to(files_dir))
                files.append({"path": rel, "bytes": p.stat().st_size})
        return {
            "success": True, "action": "list_files", "project": pid,
            "files": files,
            "count": len(files),
            "message": f"{len(files)} file(s) in project.",
            "error": None,
        }

    # ── Action: delete_file ───────────────────────────────────────────────────

    def _delete_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "").strip()
        if not filename:
            return self._err(pid, "delete_file", "'filename' is required.")
        try:
            target = _safe_relpath(files_dir, filename)
        except ValueError as e:
            return self._err(pid, "delete_file", str(e))
        if not target.exists():
            return self._err(pid, "delete_file", f"File not found: {filename!r}")
        target.unlink()
        return {
            "success": True, "action": "delete_file", "project": pid,
            "filename": filename,
            "message": f"Deleted {filename}.",
            "error": None,
        }

    # ── Action: install_package ───────────────────────────────────────────────

    def _install_package(self, pid: str, venv_dir: Path, params: dict) -> dict:
        package = params.get("package", "").strip()
        if not package:
            return self._err(pid, "install_package", "'package' is required.")

        # Reject shell-injection attempts in package name
        if any(c in package for c in (";", "&", "|", "`", "$", "\n", "\r", " ")):
            return self._err(pid, "install_package",
                f"Invalid package name: {package!r}")

        pip_exe = self._ensure_venv(venv_dir)

        cmd = [str(pip_exe), "install", "--quiet", "--disable-pip-version-check", package]
        t0  = time.perf_counter()

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=PIP_TIMEOUT_SECONDS,
            env=_clean_env(),
        )
        elapsed_ms = round((time.perf_counter() - t0) * 1000)

        if result.returncode != 0:
            return {
                "success": False, "action": "install_package", "project": pid,
                "package": package,
                "stdout": _truncate(result.stdout),
                "stderr": _truncate(result.stderr),
                "elapsed_ms": elapsed_ms,
                "message": f"pip install {package} failed (exit {result.returncode}).",
                "error": result.stderr.strip() or "pip exited non-zero",
            }

        return {
            "success": True, "action": "install_package", "project": pid,
            "package": package,
            "stdout": _truncate(result.stdout),
            "elapsed_ms": elapsed_ms,
            "message": f"Installed {package} in {elapsed_ms}ms.",
            "error": None,
        }

    # ── Action: list_packages ─────────────────────────────────────────────────

    def _list_packages(self, pid: str, venv_dir: Path) -> dict:
        if not venv_dir.exists():
            return {
                "success": True, "action": "list_packages", "project": pid,
                "packages": [],
                "message": "No venv yet — no packages installed.",
                "error": None,
            }
        pip_exe = self._get_pip(venv_dir)
        result  = subprocess.run(
            [str(pip_exe), "list", "--format=json", "--disable-pip-version-check"],
            capture_output=True, text=True, timeout=30, env=_clean_env(),
        )
        try:
            pkgs = json.loads(result.stdout)
        except json.JSONDecodeError:
            pkgs = []
        return {
            "success": True, "action": "list_packages", "project": pid,
            "packages": pkgs,
            "count": len(pkgs),
            "message": f"{len(pkgs)} package(s) installed.",
            "error": None,
        }

    # ── Action: run ───────────────────────────────────────────────────────────

    def _run_file(self, pid: str, files_dir: Path, venv_dir: Path, params: dict) -> dict:
        filename  = params.get("filename", "").strip()
        entry_args = params.get("entry_args", [])

        if not filename:
            return self._err(pid, "run", "'filename' is required.")
        if not filename.endswith(".py"):
            return self._err(pid, "run", "Only .py files can be executed.")
        try:
            target = _safe_relpath(files_dir, filename)
        except ValueError as e:
            return self._err(pid, "run", str(e))
        if not target.exists():
            return self._err(pid, "run", f"File not found: {filename!r}")

        python_exe = self._ensure_python(venv_dir)
        cmd = [str(python_exe), str(target)] + [str(a) for a in entry_args]

        return self._subprocess_run(pid, "run", cmd, cwd=files_dir, filename=filename)

    # ── Action: run_snippet ───────────────────────────────────────────────────

    def _run_snippet(self, pid: str, files_dir: Path, venv_dir: Path, params: dict) -> dict:
        code = params.get("code", "").strip()
        if not code:
            return self._err(pid, "run_snippet", "'code' is required.")

        python_exe = self._ensure_python(venv_dir)

        # Wrap snippet so project files/ is on sys.path
        wrapper = textwrap.dedent(f"""\
            import sys, os
            sys.path.insert(0, {str(files_dir)!r})
            os.chdir({str(files_dir)!r})
            exec(compile({code!r}, '<snippet>', 'exec'))
        """)

        cmd = [str(python_exe), "-c", wrapper]
        return self._subprocess_run(pid, "run_snippet", cmd, cwd=files_dir)

    # ── Action: reset ─────────────────────────────────────────────────────────

    def _reset(self, pid: str, project_dir: Path) -> dict:
        if project_dir.exists():
            shutil.rmtree(project_dir)
        return {
            "success": True, "action": "reset", "project": pid,
            "message": f"Project '{pid}' deleted. Next write_file will start fresh.",
            "error": None,
        }

    # ── Action: status ────────────────────────────────────────────────────────

    def _status(self, pid: str, project_dir: Path, files_dir: Path, venv_dir: Path) -> dict:
        files_info    = self._list_files(pid, files_dir)
        packages_info = self._list_packages(pid, venv_dir)
        return {
            "success": True, "action": "status", "project": pid,
            "project_root": str(project_dir),
            "files_dir":    str(files_dir),
            "venv_dir":     str(venv_dir),
            "venv_exists":  venv_dir.exists(),
            "files":        files_info.get("files", []),
            "file_count":   files_info.get("count", 0),
            "packages":     packages_info.get("packages", []),
            "package_count": packages_info.get("count", 0),
            "message": (
                f"{files_info.get('count', 0)} file(s), "
                f"{packages_info.get('count', 0)} package(s)."
            ),
            "error": None,
        }

    # ── Subprocess execution helper ───────────────────────────────────────────

    def _subprocess_run(
        self, pid: str, action: str, cmd: list,
        cwd: Path, filename: str | None = None,
    ) -> dict:
        t0 = time.perf_counter()
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=RUN_TIMEOUT_SECONDS,
                cwd=str(cwd),
                env=_clean_env(),
                # shell=False is the default — explicit for clarity
                shell=False,
            )
        except subprocess.TimeoutExpired:
            return {
                "success": False, "action": action, "project": pid,
                "filename": filename,
                "stdout": "", "stderr": "",
                "returncode": -1,
                "elapsed_ms": RUN_TIMEOUT_SECONDS * 1000,
                "message": f"Timeout: execution exceeded {RUN_TIMEOUT_SECONDS}s.",
                "error": "TimeoutExpired",
            }

        elapsed_ms = round((time.perf_counter() - t0) * 1000)

        # Append to run.log (for the human; not returned to agent)
        self._append_log(pid, cmd, result, elapsed_ms)

        return {
            "success":    result.returncode == 0,
            "action":     action,
            "project":    pid,
            "filename":   filename,
            "stdout":     _truncate(result.stdout),
            "stderr":     _truncate(result.stderr),
            "returncode": result.returncode,
            "elapsed_ms": elapsed_ms,
            "message": (
                f"Exited {result.returncode} in {elapsed_ms}ms."
                if result.returncode != 0
                else f"Ran successfully in {elapsed_ms}ms."
            ),
            "error": (
                result.stderr.strip() or f"Non-zero exit: {result.returncode}"
                if result.returncode != 0 else None
            ),
        }

    # ── Venv management ───────────────────────────────────────────────────────

    def _ensure_venv(self, venv_dir: Path) -> Path:
        """Create venv if missing. Returns path to pip executable."""
        if not venv_dir.exists():
            venv.create(str(venv_dir), with_pip=True, clear=False)
        return self._get_pip(venv_dir)

    def _ensure_python(self, venv_dir: Path) -> Path:
        """Create venv if missing. Returns path to python executable."""
        if not venv_dir.exists():
            venv.create(str(venv_dir), with_pip=True, clear=False)
        return self._get_python(venv_dir)

    @staticmethod
    def _get_pip(venv_dir: Path) -> Path:
        for candidate in ("bin/pip", "bin/pip3", "Scripts/pip.exe", "Scripts/pip3.exe"):
            p = venv_dir / candidate
            if p.exists():
                return p
        raise FileNotFoundError(f"pip not found in venv: {venv_dir}")

    @staticmethod
    def _get_python(venv_dir: Path) -> Path:
        for candidate in ("bin/python", "bin/python3", "Scripts/python.exe"):
            p = venv_dir / candidate
            if p.exists():
                return p
        raise FileNotFoundError(f"python not found in venv: {venv_dir}")

    # ── Run log (human-facing) ────────────────────────────────────────────────

    def _append_log(self, pid: str, cmd: list, result, elapsed_ms: int) -> None:
        log_path = self.base_dir / pid / "run.log"
        try:
            from datetime import datetime
            ts   = datetime.now().isoformat(timespec="seconds")
            line = (
                f"[{ts}] exit={result.returncode} ms={elapsed_ms} "
                f"cmd={cmd[0]} {' '.join(cmd[1:])}\n"
            )
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(line)
                if result.stderr.strip():
                    f.write("  stderr: " + result.stderr.strip()[:200] + "\n")
        except OSError:
            pass  # never crash on logging failure

    # ── Error helper ──────────────────────────────────────────────────────────

    @staticmethod
    def _err(pid: str, action: str, message: str) -> dict:
        return {
            "success": False, "action": action, "project": pid,
            "message": message, "error": message,
        }

    # ── Project ID validation ─────────────────────────────────────────────────

    @staticmethod
    def _validate_project_id(pid: str) -> str | None:
        if not pid:
            return "'project_id' is required."
        if len(pid) > 40:
            return f"'project_id' must be ≤ 40 characters, got {len(pid)}."
        import re
        if not re.fullmatch(r"[a-zA-Z0-9_\-]+", pid):
            return f"'project_id' may only contain letters, digits, hyphens, underscores. Got: {pid!r}"
        return None
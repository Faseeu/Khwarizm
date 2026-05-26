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

from __future__ import annotations

from tools.basetool import BaseTool

import json
import logging
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
import venv
from datetime import datetime
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


# ── Tunables ──────────────────────────────────────────────────────────────────

DEFAULT_BASE_DIR      = ".agent_projects"
RUN_TIMEOUT_SECONDS   = 60
PIP_TIMEOUT_SECONDS   = 120
MAX_OUTPUT_CHARS      = 100_000
MAX_FILE_SIZE_BYTES   = 1_000_000   # 1 MB
MAX_FILES_PER_PROJECT = 100
MAX_LOG_LINES         = 10_000


# ── Validation patterns ───────────────────────────────────────────────────────

# PEP 508 distribution name plus optional version specifier
_PKG_NAME_RE = re.compile(
    r"^([A-Za-z0-9]([A-Za-z0-9._-]*[A-Za-z0-9])?)"
    r"(\s*[><=!~^]+\s*[A-Za-z0-9.*+!-]+)?$"
)

_PROJECT_ID_RE = re.compile(r"^[a-zA-Z0-9_\-]{1,40}$")

# Allowed shapes for entry_args: plain values, flags, key=value pairs
_SAFE_ARG_RE = re.compile(r"^[A-Za-z0-9_./:@,=+\-]{1,256}$")


# ── Allowed actions ───────────────────────────────────────────────────────────

ACTIONS = {
    "write_file":      "Create or overwrite a file in the project.",
    "read_file":       "Read a file from the project.",
    "list_files":      "List all files in the project.",
    "delete_file":     "Delete a file from the project.",
    "move_file":       "Move or rename a file within the project.",
    "install_package": "Install a pip package into the project venv.",
    "list_packages":   "List packages installed in the project venv.",
    "run":             "Execute a Python file inside the project venv.",
    "run_snippet":     "Run an ad-hoc Python snippet inside the project venv.",
    "reset":           "Delete the entire project directory and start fresh.",
    "status":          "Return project metadata (files, packages, venv path).",
}


# ── Custom exceptions ─────────────────────────────────────────────────────────

class ProjectRunnerError(Exception):
    """Base for all tool-level errors."""

class PathTraversalError(ProjectRunnerError):
    """Raised when a path escapes the project root."""

class ValidationError(ProjectRunnerError):
    """Raised when input parameters fail validation."""

class VenvError(ProjectRunnerError):
    """Raised when venv creation or executable lookup fails."""


# ── Helpers ───────────────────────────────────────────────────────────────────

def _clean_env(venv_dir: Path) -> dict[str, str]:
    """
    Return a minimal environment for subprocesses.
    Replaces PATH with only the venv bin directory so no host
    executables are reachable. Keeps locale and temp-dir variables.
    """
    venv_bin = str(venv_dir / ("Scripts" if sys.platform == "win32" else "bin"))

    keep_as_is = {
        "HOME", "USER", "LANG", "LC_ALL", "LC_CTYPE",
        "TERM", "TMPDIR", "TMP", "TEMP",
        "SYSTEMROOT", "USERPROFILE",
    }
    env = {k: v for k, v in os.environ.items() if k in keep_as_is}
    env["PATH"] = venv_bin
    return env


def _truncate(text: str, limit: int = MAX_OUTPUT_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n[...output truncated at {limit} chars]"


def _safe_relpath(base: Path, target: str) -> Path:
    """
    Resolve *target* relative to *base* and verify it stays inside *base*.
    Raises PathTraversalError on traversal attempts.
    Raises ValidationError on empty or obviously invalid paths.
    """
    if not target or target.strip() in ("", ".", ".."):
        raise ValidationError(f"Invalid path: {target!r}")
    resolved = (base / target).resolve()
    try:
        resolved.relative_to(base.resolve())
    except ValueError:
        raise PathTraversalError(
            f"Path traversal blocked: {target!r} escapes project root."
        )
    return resolved


def _validate_project_id(pid: str) -> str | None:
    """Return an error message string, or None if valid."""
    if not pid:
        return "'project_id' is required."
    if not _PROJECT_ID_RE.fullmatch(pid):
        return (
            f"'project_id' must be 1-40 characters: letters, digits, "
            f"hyphens, underscores. Got: {pid!r}"
        )
    return None


def _validate_package_name(package: str) -> str | None:
    """Return an error message string, or None if valid."""
    if not package:
        return "'package' is required."
    if not _PKG_NAME_RE.fullmatch(package.strip()):
        return (
            f"Invalid package specifier: {package!r}. "
            "Use PyPI names like 'requests' or 'pandas==2.2.0'."
        )
    return None


def _validate_entry_args(args: Any) -> tuple[list[str], str | None]:
    """
    Validate and normalise entry_args.
    Returns (clean_list, error_message_or_None).
    """
    if args is None:
        return [], None
    if not isinstance(args, list):
        return [], "'entry_args' must be a list of strings."
    clean = []
    for i, arg in enumerate(args):
        arg_str = str(arg)
        if not _SAFE_ARG_RE.fullmatch(arg_str):
            return [], (
                f"entry_args[{i}]={arg_str!r} contains unsafe characters. "
                "Only alphanumerics and _./:@,=+- are allowed."
            )
        clean.append(arg_str)
    return clean, None


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
        run.log         ← rotating log of every run (not returned to agent)
    """

    def __init__(self, base_dir: str = DEFAULT_BASE_DIR) -> None:
        self.base_dir = Path(base_dir).resolve()
        self.base_dir.mkdir(parents=True, exist_ok=True)

        self.name = "project_runner"
        self.description = (
            "Manage and execute a full multi-file Python project with pip package support. "
            "Actions: write_file, read_file, list_files, delete_file, move_file, "
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
                "[write_file, read_file, delete_file, run, move_file (source)] "
                "Path relative to the project root, e.g. 'main.py' or 'utils/helpers.py'."
            ),
            "destination": (
                "[move_file] Destination path relative to the project root."
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
                "e.g. ['--input', 'data.csv']. Each arg must match "
                r"^[A-Za-z0-9_./:@,=+\-]{1,256}$. Defaults to []."
            ),
            "stdin": (
                "[run] Optional string to feed as stdin to the process."
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
        project_id = parameters.get("project_id", "")
        if isinstance(project_id, str):
            project_id = project_id.strip()

        action = parameters.get("action", "")
        if isinstance(action, str):
            action = action.strip()

        # ── Validate project_id ───────────────────────────────────────
        pid_err = _validate_project_id(project_id)
        if pid_err:
            return self._err(project_id, action, pid_err)

        # ── Validate action ───────────────────────────────────────────
        if action not in ACTIONS:
            return self._err(
                project_id, action,
                f"Unknown action {action!r}. Valid actions: {', '.join(ACTIONS)}"
            )

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
            elif action == "move_file":
                return self._move_file(project_id, files_dir, parameters)
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
        except ProjectRunnerError as exc:
            return self._err(project_id, action, str(exc))
        except Exception as exc:
            import traceback
            logger.exception("Unexpected error in ProjectRunnerTool")
            return self._err(
                project_id, action,
                f"Unexpected error: {exc}\n{traceback.format_exc()}"
            )

    # ── Action: write_file ────────────────────────────────────────────────────

    def _write_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "")
        if isinstance(filename, str):
            filename = filename.strip()
        content = params.get("content", "")

        if not filename:
            return self._err(pid, "write_file", "'filename' is required.")
        if not isinstance(content, str):
            return self._err(pid, "write_file", "'content' must be a string.")

        encoded = content.encode("utf-8")
        if len(encoded) > MAX_FILE_SIZE_BYTES:
            return self._err(
                pid, "write_file",
                f"File exceeds size limit ({MAX_FILE_SIZE_BYTES // 1_000} KB)."
            )

        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "write_file", str(e))

        # Count only regular files, and only block if this is a brand new file
        existing_count = sum(1 for p in files_dir.rglob("*") if p.is_file())
        is_new_file = not target.exists()
        if is_new_file and existing_count >= MAX_FILES_PER_PROJECT:
            return self._err(
                pid, "write_file",
                f"Project file limit ({MAX_FILES_PER_PROJECT}) reached."
            )

        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

        return {
            "success":       True,
            "action":        "write_file",
            "project":       pid,
            "filename":      filename,
            "bytes_written": len(encoded),
            "path":          str(target),
            "message":       f"Wrote {filename} ({len(encoded):,} bytes).",
            "error":         None,
        }

    # ── Action: read_file ─────────────────────────────────────────────────────

    def _read_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "").strip()
        if not filename:
            return self._err(pid, "read_file", "'filename' is required.")
        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "read_file", str(e))

        if not target.exists():
            return self._err(pid, "read_file", f"File not found: {filename!r}")
        if not target.is_file():
            return self._err(pid, "read_file", f"Not a file: {filename!r}")

        content    = target.read_text(encoding="utf-8")
        byte_count = len(content.encode("utf-8"))
        return {
            "success":  True,
            "action":   "read_file",
            "project":  pid,
            "filename": filename,
            "content":  content,
            "bytes":    byte_count,
            "message":  f"Read {filename} ({byte_count:,} bytes).",
            "error":    None,
        }

    # ── Action: list_files ────────────────────────────────────────────────────

    def _list_files(self, pid: str, files_dir: Path) -> dict:
        if not files_dir.exists():
            return {
                "success": True, "action": "list_files", "project": pid,
                "files": [], "count": 0,
                "message": "Project is empty.", "error": None,
            }
        files = []
        for p in sorted(files_dir.rglob("*")):
            if p.is_file():
                rel  = p.relative_to(files_dir).as_posix()
                stat = p.stat()
                files.append({
                    "path":     rel,
                    "bytes":    stat.st_size,
                    "modified": datetime.fromtimestamp(
                        stat.st_mtime
                    ).isoformat(timespec="seconds"),
                })
        return {
            "success": True, "action": "list_files", "project": pid,
            "files":   files,
            "count":   len(files),
            "message": f"{len(files)} file(s) in project.",
            "error":   None,
        }

    # ── Action: delete_file ───────────────────────────────────────────────────

    def _delete_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        filename = params.get("filename", "").strip()
        if not filename:
            return self._err(pid, "delete_file", "'filename' is required.")
        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "delete_file", str(e))

        if not target.exists():
            return self._err(pid, "delete_file", f"File not found: {filename!r}")
        if not target.is_file():
            return self._err(pid, "delete_file", f"Not a file: {filename!r}")

        target.unlink()
        return {
            "success":  True,
            "action":   "delete_file",
            "project":  pid,
            "filename": filename,
            "message":  f"Deleted {filename}.",
            "error":    None,
        }

    # ── Action: move_file ─────────────────────────────────────────────────────

    def _move_file(self, pid: str, files_dir: Path, params: dict) -> dict:
        src_name = params.get("filename", "").strip()
        dst_name = params.get("destination", "").strip()

        if not src_name:
            return self._err(pid, "move_file", "'filename' (source) is required.")
        if not dst_name:
            return self._err(pid, "move_file", "'destination' is required.")

        try:
            src = _safe_relpath(files_dir, src_name)
            dst = _safe_relpath(files_dir, dst_name)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "move_file", str(e))

        if not src.exists():
            return self._err(pid, "move_file", f"Source not found: {src_name!r}")
        if not src.is_file():
            return self._err(pid, "move_file", f"Not a file: {src_name!r}")
        if dst.exists():
            return self._err(pid, "move_file", f"Destination already exists: {dst_name!r}")

        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)

        return {
            "success":     True,
            "action":      "move_file",
            "project":     pid,
            "filename":    src_name,
            "destination": dst_name,
            "message":     f"Moved {src_name!r} -> {dst_name!r}.",
            "error":       None,
        }

    # ── Action: install_package ───────────────────────────────────────────────

    def _install_package(self, pid: str, venv_dir: Path, params: dict) -> dict:
        package = params.get("package", "").strip()

        pkg_err = _validate_package_name(package)
        if pkg_err:
            return self._err(pid, "install_package", pkg_err)

        pip_exe = self._ensure_venv(venv_dir)
        cmd = [
            str(pip_exe), "install",
            "--quiet",
            "--disable-pip-version-check",
            "--no-input",
            "--exists-action", "i",
            package,
        ]
        t0 = time.perf_counter()
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=PIP_TIMEOUT_SECONDS,
                env=_clean_env(venv_dir),
                shell=False,
            )
        except subprocess.TimeoutExpired:
            return self._err(
                pid, "install_package",
                f"pip install timed out after {PIP_TIMEOUT_SECONDS}s."
            )

        elapsed_ms = round((time.perf_counter() - t0) * 1000)

        if result.returncode != 0:
            return {
                "success":    False,
                "action":     "install_package",
                "project":    pid,
                "package":    package,
                "stdout":     _truncate(result.stdout),
                "stderr":     _truncate(result.stderr),
                "elapsed_ms": elapsed_ms,
                "message":    f"pip install {package!r} failed (exit {result.returncode}).",
                "error":      result.stderr.strip() or f"exit {result.returncode}",
            }

        return {
            "success":    True,
            "action":     "install_package",
            "project":    pid,
            "package":    package,
            "stdout":     _truncate(result.stdout),
            "elapsed_ms": elapsed_ms,
            "message":    f"Installed {package!r} in {elapsed_ms} ms.",
            "error":      None,
        }

    # ── Action: list_packages ─────────────────────────────────────────────────

    def _list_packages(self, pid: str, venv_dir: Path) -> dict:
        if not venv_dir.exists():
            return {
                "success":  True,
                "action":   "list_packages",
                "project":  pid,
                "packages": [],
                "count":    0,
                "message":  "No venv yet — no packages installed.",
                "error":    None,
            }
        pip_exe = self._get_pip(venv_dir)
        result  = subprocess.run(
            [str(pip_exe), "list", "--format=json", "--disable-pip-version-check"],
            capture_output=True, text=True, timeout=30,
            env=_clean_env(venv_dir), shell=False,
        )
        warning = None
        try:
            pkgs = json.loads(result.stdout)
        except json.JSONDecodeError:
            pkgs    = []
            warning = f"Could not parse pip list output: {result.stdout[:200]!r}"
            logger.warning("list_packages JSON parse failure: %s", result.stdout[:200])

        return {
            "success":  True,
            "action":   "list_packages",
            "project":  pid,
            "packages": pkgs,
            "count":    len(pkgs),
            "message":  f"{len(pkgs)} package(s) installed.",
            "warning":  warning,
            "error":    None,
        }

    # ── Action: run ───────────────────────────────────────────────────────────

    def _run_file(
        self, pid: str, files_dir: Path, venv_dir: Path, params: dict
    ) -> dict:
        filename   = params.get("filename", "").strip()
        entry_args = params.get("entry_args", [])
        stdin_data = params.get("stdin", None)

        if not filename:
            return self._err(pid, "run", "'filename' is required.")
        if not filename.endswith(".py"):
            return self._err(pid, "run", "Only .py files can be executed.")

        try:
            target = _safe_relpath(files_dir, filename)
        except (PathTraversalError, ValidationError) as e:
            return self._err(pid, "run", str(e))

        if not target.exists():
            return self._err(pid, "run", f"File not found: {filename!r}")
        if not target.is_file():
            return self._err(pid, "run", f"Not a file: {filename!r}")

        clean_args, args_err = _validate_entry_args(entry_args)
        if args_err:
            return self._err(pid, "run", args_err)

        python_exe = self._ensure_python(venv_dir)
        cmd = [str(python_exe), str(target)] + clean_args

        return self._subprocess_run(
            pid, "run", cmd, cwd=files_dir,
            filename=filename, stdin_data=stdin_data,
            venv_dir=venv_dir,
        )

    # ── Action: run_snippet ───────────────────────────────────────────────────

    def _run_snippet(
        self, pid: str, files_dir: Path, venv_dir: Path, params: dict
    ) -> dict:
        """
        Execute an ad-hoc snippet by writing it to a temp file — never
        embedding it in a shell string or -c argument.
        Tracebacks will show real line numbers inside the snippet.
        """
        code = params.get("code", "")
        if not isinstance(code, str) or not code.strip():
            return self._err(pid, "run_snippet", "'code' must be a non-empty string.")

        python_exe = self._ensure_python(venv_dir)

        # Wrapper gives the snippet access to project files on sys.path
        wrapper = textwrap.dedent(f"""\
            import sys as _sys, os as _os
            _sys.path.insert(0, {str(files_dir)!r})
            _os.chdir({str(files_dir)!r})
            # ── user snippet below ──────────────────────────────────
        """) + code

        # Write to a real temp file so tracebacks show accurate line numbers
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", prefix="snippet_",
            dir=str(files_dir), delete=False, encoding="utf-8",
        ) as tmp:
            tmp.write(wrapper)
            tmp_path = Path(tmp.name)

        try:
            cmd = [str(python_exe), str(tmp_path)]
            return self._subprocess_run(
                pid, "run_snippet", cmd, cwd=files_dir, venv_dir=venv_dir
            )
        finally:
            try:
                tmp_path.unlink()
            except OSError:
                pass

    # ── Action: reset ─────────────────────────────────────────────────────────

    def _reset(self, pid: str, project_dir: Path) -> dict:
        existed = project_dir.exists()
        if existed:
            shutil.rmtree(project_dir)
        return {
            "success": True,
            "action":  "reset",
            "project": pid,
            "message": (
                f"Project '{pid}' deleted. Next write_file will start fresh."
                if existed else
                f"Project '{pid}' did not exist — nothing to delete."
            ),
            "error": None,
        }

    # ── Action: status ────────────────────────────────────────────────────────

    def _status(
        self, pid: str, project_dir: Path, files_dir: Path, venv_dir: Path
    ) -> dict:
        files_info = self._list_files(pid, files_dir)
        # Only call list_packages if venv actually exists
        packages_info = (
            self._list_packages(pid, venv_dir)
            if venv_dir.exists()
            else {"packages": [], "count": 0}
        )
        return {
            "success":       True,
            "action":        "status",
            "project":       pid,
            "project_root":  str(project_dir),
            "files_dir":     str(files_dir),
            "venv_dir":      str(venv_dir),
            "venv_exists":   venv_dir.exists(),
            "files":         files_info.get("files", []),
            "file_count":    files_info.get("count", 0),
            "packages":      packages_info.get("packages", []),
            "package_count": packages_info.get("count", 0),
            "message": (
                f"{files_info.get('count', 0)} file(s), "
                f"{packages_info.get('count', 0)} package(s)."
            ),
            "error": None,
        }

    # ── Subprocess execution helper ───────────────────────────────────────────

    def _subprocess_run(
        self,
        pid: str,
        action: str,
        cmd: list[str],
        cwd: Path,
        filename: str | None = None,
        stdin_data: str | None = None,
        venv_dir: Path | None = None,
    ) -> dict:
        env = _clean_env(venv_dir) if venv_dir else dict(os.environ)
        t0  = time.perf_counter()

        try:
            result = subprocess.run(
                cmd,
                input=stdin_data,
                capture_output=True,
                text=True,
                timeout=RUN_TIMEOUT_SECONDS,
                cwd=str(cwd),
                env=env,
                shell=False,
            )
        except subprocess.TimeoutExpired:
            return {
                "success":    False,
                "action":     action,
                "project":    pid,
                "filename":   filename,
                "stdout":     "",
                "stderr":     "",
                "returncode": -1,
                "elapsed_ms": RUN_TIMEOUT_SECONDS * 1_000,
                "message":    f"Timeout: execution exceeded {RUN_TIMEOUT_SECONDS}s.",
                "error":      "TimeoutExpired",
            }

        elapsed_ms = round((time.perf_counter() - t0) * 1000)
        self._append_log(pid, cmd, result, elapsed_ms)

        success = result.returncode == 0
        return {
            "success":    success,
            "action":     action,
            "project":    pid,
            "filename":   filename,
            "stdout":     _truncate(result.stdout),
            "stderr":     _truncate(result.stderr),
            "returncode": result.returncode,
            "elapsed_ms": elapsed_ms,
            "message": (
                f"Ran successfully in {elapsed_ms} ms."
                if success else
                f"Exited {result.returncode} in {elapsed_ms} ms."
            ),
            "error": (
                None if success else
                (result.stderr.strip() or f"Non-zero exit: {result.returncode}")
            ),
        }

    # ── Venv management ───────────────────────────────────────────────────────

    def _ensure_venv(self, venv_dir: Path) -> Path:
        """Create venv if missing. Returns path to pip executable."""
        if not venv_dir.exists():
            try:
                venv.create(str(venv_dir), with_pip=True, clear=False)
            except Exception as exc:
                raise VenvError(
                    f"Failed to create venv at {venv_dir}: {exc}"
                ) from exc
        return self._get_pip(venv_dir)

    def _ensure_python(self, venv_dir: Path) -> Path:
        """Create venv if missing. Returns path to python executable."""
        if not venv_dir.exists():
            try:
                venv.create(str(venv_dir), with_pip=True, clear=False)
            except Exception as exc:
                raise VenvError(
                    f"Failed to create venv at {venv_dir}: {exc}"
                ) from exc
        return self._get_python(venv_dir)

    @staticmethod
    def _get_pip(venv_dir: Path) -> Path:
        for candidate in (
            "bin/pip", "bin/pip3",
            "Scripts/pip.exe", "Scripts/pip3.exe",
        ):
            p = venv_dir / candidate
            if p.exists():
                return p
        raise VenvError(f"pip not found in venv: {venv_dir}")

    @staticmethod
    def _get_python(venv_dir: Path) -> Path:
        for candidate in (
            "bin/python", "bin/python3",
            "Scripts/python.exe",
        ):
            p = venv_dir / candidate
            if p.exists():
                return p
        raise VenvError(f"python not found in venv: {venv_dir}")

    # ── Run log ───────────────────────────────────────────────────────────────

    def _append_log(
        self,
        pid: str,
        cmd: list[str],
        result: subprocess.CompletedProcess,
        elapsed_ms: int,
    ) -> None:
        """
        Append one entry to run.log.
        Rotates the file when it exceeds MAX_LOG_LINES to prevent
        unbounded disk growth.
        """
        log_path = self.base_dir / pid / "run.log"
        try:
            ts   = datetime.now().isoformat(timespec="seconds")
            line = (
                f"[{ts}] exit={result.returncode} ms={elapsed_ms} "
                f"cmd={' '.join(cmd)}\n"
            )
            stderr_line = (
                ("  stderr: " + result.stderr.strip()[:200] + "\n")
                if result.stderr.strip() else ""
            )

            # Rotate if the log has grown too large
            if log_path.exists():
                lines = log_path.read_text(
                    encoding="utf-8", errors="replace"
                ).splitlines(keepends=True)
                if len(lines) >= MAX_LOG_LINES:
                    keep = lines[MAX_LOG_LINES // 2:]
                    log_path.write_text("".join(keep), encoding="utf-8")

            with log_path.open("a", encoding="utf-8") as f:
                f.write(line)
                if stderr_line:
                    f.write(stderr_line)

        except OSError as exc:
            logger.warning(
                "Could not write run.log for project %r: %s", pid, exc
            )

    # ── Error helper ──────────────────────────────────────────────────────────

    @staticmethod
    def _err(pid: str, action: str, message: str) -> dict:
        return {
            "success": False,
            "action":  action,
            "project": pid,
            "message": message,
            "error":   message,
        }

        # i want you to study all of the project except for the .md and offcourse the ones mentioned in the .gitignore file the thing is that the main dir has been polluted by a lot of files not that i mind but they wll create a mess but if we dont do something about allthe shit we have. we have to somehow categorize those files somewhere right. create a plan.md file and show me what we can do
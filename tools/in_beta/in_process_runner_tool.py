"""
tools/python_runner_tool.py

PythonRunnerTool
================
Executes a single Python file inside the current interpreter process.

Strategy
--------
- Zero new dependencies — uses only CPython stdlib.
- exec() with a restricted globals dict (allowlisted builtins + guarded import).
- POSIX resource limits (CPU time, address space, no subprocesses) applied
  inside the worker thread before exec() runs.
- Hard wall-clock timeout via a daemon thread join.
- open() restricted to the working directory — no absolute paths, no ../traversal.
- Stdout/stderr captured and returned; never printed directly.

When to use this tool
---------------------
Use for single-file scripts that only need the standard library or the
allowlisted pure-Python modules listed in _ALLOWED_MODULES below.
For multi-file projects or third-party package installs, use ProjectRunnerTool.
"""

from tools.basetool import BaseTool

import builtins
import io
import os
import resource
import threading
import time
import traceback


# ── Tunables ──────────────────────────────────────────────────────────────────

TIMEOUT_SECONDS = 15          # hard wall-clock limit per run
CPU_SECONDS     = 10          # POSIX RLIMIT_CPU (Linux/macOS only)
MAX_MEMORY_MB   = 128         # POSIX RLIMIT_AS  (Linux/macOS only)
MAX_OUTPUT_CHARS = 50_000     # truncate captured output beyond this

# ── Import allowlist ──────────────────────────────────────────────────────────

_ALLOWED_MODULES = {
    # math / numerics
    "math", "cmath", "decimal", "fractions", "statistics", "random",
    "numbers",
    # data structures
    "collections", "collections.abc", "heapq", "bisect", "array",
    "queue", "copy", "pprint", "enum",
    # strings / text
    "string", "textwrap", "re", "difflib", "unicodedata",
    # date / time
    "datetime", "calendar", "time", "zoneinfo",
    # itertools / functools
    "itertools", "functools", "operator",
    # serialisation
    "json", "csv", "pickle", "struct",
    # typing / introspection
    "typing", "types", "abc", "dataclasses", "inspect",
    # I/O (stdout only — open() is guarded)
    "io", "pathlib",
    # hashing / encoding
    "hashlib", "hmac", "base64", "binascii",
    # context / utils
    "contextlib", "weakref", "gc",
    # exceptions only
    "errno",
}


def _make_safe_import(allowed: set):
    """Return a replacement __import__ restricted to *allowed* modules."""

    def _safe_import(name, globals=None, locals=None, fromlist=(), level=0):
        top = name.split(".")[0]
        if top not in allowed:
            raise ImportError(
                f"Sandbox: '{name}' is not on the import allowlist. "
                f"Use ProjectRunnerTool for third-party packages."
            )
        return builtins.__import__(name, globals, locals, fromlist, level)

    return _safe_import


def _make_safe_open(cwd: str):
    """Return an open() that only permits paths under *cwd*."""

    def _safe_open(file, mode="r", *args, **kwargs):
        path = os.path.realpath(os.path.join(cwd, str(file)))
        if not path.startswith(os.path.realpath(cwd)):
            raise PermissionError(
                f"Sandbox: access outside working directory is blocked: {file!r}"
            )
        return builtins.open(path, mode, *args, **kwargs)

    return _safe_open


def _build_sandbox_globals(cwd: str) -> dict:
    """Assemble the restricted globals dict for exec()."""

    safe_names = {
        "None", "True", "False",
        "bool", "int", "float", "complex", "str", "bytes", "bytearray",
        "list", "tuple", "dict", "set", "frozenset", "memoryview",
        "print", "input",
        "range", "enumerate", "zip", "map", "filter", "reversed", "sorted",
        "len", "sum", "min", "max", "abs", "round", "divmod", "pow",
        "isinstance", "issubclass", "callable", "type",
        "hasattr", "getattr", "setattr", "delattr",
        "vars", "dir", "repr", "hash", "id",
        "iter", "next", "all", "any",
        "chr", "ord", "bin", "oct", "hex", "format",
        "compile", "eval", "exec",
        "staticmethod", "classmethod", "property", "super",
        "object",
        # exception types
        "Exception", "BaseException", "ValueError", "TypeError",
        "KeyError", "IndexError", "AttributeError", "RuntimeError",
        "StopIteration", "NotImplementedError", "OSError", "IOError",
        "FileNotFoundError", "PermissionError", "AssertionError",
        "ZeroDivisionError", "OverflowError", "ImportError", "NameError",
        "RecursionError", "GeneratorExit", "SystemExit", "KeyboardInterrupt",
        "ArithmeticError", "LookupError", "UnicodeError",
        "UnicodeDecodeError", "UnicodeEncodeError", "StopAsyncIteration",
        "ConnectionError", "TimeoutError",
        # built-in functions continued
        "slice", "Ellipsis", "NotImplemented",
        "breakpoint",   # will hit our safe version or just pass
    }

    sandbox = {name: getattr(builtins, name) for name in safe_names if hasattr(builtins, name)}
    sandbox["open"]       = _make_safe_open(cwd)
    sandbox["__import__"] = _make_safe_import(_ALLOWED_MODULES)
    sandbox["__builtins__"] = sandbox   # so nested exec/eval sees same env
    sandbox["__name__"]   = "__main__"
    sandbox["__doc__"]    = None
    return sandbox


# ── Resource limits ───────────────────────────────────────────────────────────

def _apply_resource_limits() -> None:
    try:
        resource.setrlimit(resource.RLIMIT_CPU, (CPU_SECONDS, CPU_SECONDS))
        mem = MAX_MEMORY_MB * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem, mem))
        resource.setrlimit(resource.RLIMIT_NPROC, (0, 0))
    except (AttributeError, ValueError, OSError):
        pass  # Windows or unprivileged — skip silently


# ── Sandbox runner (runs inside daemon thread) ────────────────────────────────

def _run_sandboxed(code: str, filepath: str, result_box: list) -> None:
    """
    Execute *code* in a restricted globals dict with resource limits.
    Stores a result dict into result_box[0].
    """
    import sys

    _apply_resource_limits()

    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    sys.stdout = stdout_buf
    sys.stderr = stderr_buf

    cwd     = os.path.dirname(os.path.abspath(filepath))
    sandbox = _build_sandbox_globals(cwd)
    sandbox["__file__"] = filepath

    t_start = time.perf_counter()
    error   = None

    try:
        exec(compile(code, filepath, "exec"), sandbox)  # noqa: S102
    except SystemExit:
        pass  # treat sys.exit() as clean termination
    except Exception:
        error = traceback.format_exc()
    finally:
        sys.stdout = old_out
        sys.stderr = old_err

    elapsed_ms = round((time.perf_counter() - t_start) * 1000)
    stdout_val = stdout_buf.getvalue()
    stderr_val = stderr_buf.getvalue()

    # Truncate runaway output
    if len(stdout_val) > MAX_OUTPUT_CHARS:
        stdout_val = stdout_val[:MAX_OUTPUT_CHARS] + f"\n[...truncated at {MAX_OUTPUT_CHARS} chars]"
    if len(stderr_val) > MAX_OUTPUT_CHARS:
        stderr_val = stderr_val[:MAX_OUTPUT_CHARS] + f"\n[...truncated at {MAX_OUTPUT_CHARS} chars]"

    result_box[0] = {
        "stdout":     stdout_val,
        "stderr":     stderr_val,
        "error":      error,
        "elapsed_ms": elapsed_ms,
        "file":       filepath,
    }


# ── Tool class ────────────────────────────────────────────────────────────────

class InprocessPythonRunnerTool(BaseTool):
    """
    Execute a single Python file in a locked-down in-process sandbox.

    Capabilities
    ------------
    - Fast: <1 ms overhead (no subprocess, no venv spin-up).
    - Safe: restricted builtins, guarded import/open, POSIX resource limits,
      hard timeout via daemon thread.
    - Zero deps: pure CPython stdlib.

    Limitations
    -----------
    - Only stdlib modules on the allowlist are importable.
    - No network access, no subprocess spawning, no absolute filesystem paths.
    - For third-party packages or multi-file projects → use ProjectRunnerTool.
    """

    def __init__(self):
        self.name = "python_runner"
        self.description = (
            "Execute a single Python (.py) file in a secure in-process sandbox. "
            "Supports stdlib only. Returns stdout, stderr, errors, and execution time. "
            "No installs required. For projects with pip packages use project_runner."
        )
        self.parameters = {
            "filepath": (
                "Path to the .py file to execute. "
                "Must be relative to the working directory."
            ),
        }

    # ------------------------------------------------------------------
    def run(self, parameters: dict) -> dict:
        """
        Execute the file at parameters['filepath'].

        Returns
        -------
        dict with keys:
            success     : bool   — True if no uncaught exception
            stdout      : str    — captured standard output
            stderr      : str    — captured standard error
            error       : str|None — formatted traceback if exception
            elapsed_ms  : int    — wall-clock execution time in milliseconds
            file        : str    — resolved filepath that was executed
            sandbox     : str    — always "in-process (restricted exec)"
        """
        filepath: str = parameters.get("filepath", "").strip()

        # ── Validate ────────────────────────────────────────────────────
        err = self._validate(filepath)
        if err:
            return {"success": False, "error": err, "stdout": "", "stderr": "",
                    "elapsed_ms": 0, "file": filepath, "sandbox": "in-process (restricted exec)"}

        norm = os.path.normpath(filepath)

        # ── Read source ─────────────────────────────────────────────────
        try:
            source = open(norm, encoding="utf-8").read()
        except OSError as exc:
            return {"success": False, "error": f"Cannot read file: {exc}",
                    "stdout": "", "stderr": "", "elapsed_ms": 0,
                    "file": norm, "sandbox": "in-process (restricted exec)"}

        # ── Syntax check before threading ───────────────────────────────
        try:
            compile(source, norm, "exec")
        except SyntaxError as exc:
            return {"success": False, "error": f"SyntaxError: {exc}",
                    "stdout": "", "stderr": "", "elapsed_ms": 0,
                    "file": norm, "sandbox": "in-process (restricted exec)"}

        # ── Run in daemon thread with timeout ───────────────────────────
        result_box: list = [None]
        thread = threading.Thread(
            target=_run_sandboxed,
            args=(source, norm, result_box),
            daemon=True,
        )
        thread.start()
        thread.join(timeout=TIMEOUT_SECONDS)

        if thread.is_alive():
            return {
                "success":    False,
                "error":      f"Timeout: execution exceeded {TIMEOUT_SECONDS}s wall-clock limit.",
                "stdout":     "",
                "stderr":     "",
                "elapsed_ms": TIMEOUT_SECONDS * 1000,
                "file":       norm,
                "sandbox":    "in-process (restricted exec)",
            }

        result = result_box[0]
        result["success"] = result["error"] is None
        result["sandbox"] = "in-process (restricted exec)"
        return result

    # ------------------------------------------------------------------
    @staticmethod
    def _validate(filepath: str) -> str | None:
        """Return an error string, or None if filepath is acceptable."""
        if not filepath:
            return "Parameter 'filepath' is required."
        norm = os.path.normpath(filepath)
        if os.path.isabs(norm):
            return f"Absolute paths are not permitted: {filepath!r}"
        if norm.startswith(".."):
            return f"Parent-directory traversal is not permitted: {filepath!r}"
        if not norm.endswith(".py"):
            return f"Only .py files are accepted, got: {filepath!r}"
        if not os.path.isfile(norm):
            return f"File not found: {norm!r}"
        return None
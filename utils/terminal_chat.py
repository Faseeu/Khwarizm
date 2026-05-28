"""
terminal_chat.py — Terminal chat UI for BaseAgent.

Captures agent's internal stdout prints (loop counter, tool calls)
and renders them after the run completes. No threads, no polling.

Dependency: pip install rich
"""

import sys
import io
import time
import datetime
from typing import Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    from rich.rule import Rule
    from rich.markdown import Markdown
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

STYLE_USER      = "bold cyan"
STYLE_AGENT     = "bold green"
STYLE_TOOL      = "bold yellow"
STYLE_LOOP      = "dim white"
STYLE_SYSTEM    = "dim yellow"
STYLE_ERROR     = "bold red"
STYLE_TIMESTAMP = "dim white"
STYLE_META      = "dim blue"

def _now() -> str:
    return datetime.datetime.now().strftime("%H:%M:%S")

def _word_count(text: str) -> int:
    return len(text.split())


# ── Stdout capture (no lock needed — synchronous now) ─────────────────────────

class _StreamCapture(io.StringIO):
    def __init__(self):
        super().__init__()
        self._lines: list[str] = []

    def write(self, s: str):
        stripped = s.rstrip("\n").strip()
        if stripped:
            self._lines.append(stripped)

    def flush(self):
        pass

    def get_lines(self) -> list[str]:
        return self._lines


# ── Trace panel (rendered once, after run) ────────────────────────────────────

def _render_trace(console: Console, lines: list[str]):
    if not lines:
        return
    text = Text()
    for line in lines:
        if "-> Tool" in line or "Tool:" in line:
            text.append(f"  ⚙  {line}\n", style=STYLE_TOOL)
        elif "Loop" in line:
            text.append(f"  {line}\n", style=STYLE_LOOP)
        elif "error" in line.lower():
            text.append(f"  ✗  {line}\n", style=STYLE_ERROR)
        else:
            text.append(f"  {line}\n", style="dim white")
    console.print(Panel(
        text,
        title=f"[{STYLE_META}]agent trace[/]",
        border_style="dim",
        box=box.SIMPLE,
        padding=(0, 1),
    ))


# ── Fallback ──────────────────────────────────────────────────────────────────

def _plain_chat(agent) -> list:
    print("=" * 60)
    print(f"  {agent.name}  |  tools: {agent.tools}")
    print("  Commands: exit · clear · history · help")
    print("=" * 60)
    history = []
    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession ended.")
            break
        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "e", "q"):
            break
        if user_input.lower() == "clear":
            agent.clear_memory()
            continue
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
        history.append({"user": user_input, "agent": response, "ts": _now()})
    return history


HELP_TEXT = """\
[bold]Commands[/bold]
  [cyan]exit / quit / e / q[/cyan]  — end the session
  [cyan]clear[/cyan]                — wipe agent memory (STM + LTM)
  [cyan]history[/cyan]              — print this session's transcript
  [cyan]help[/cyan]                 — show this message
  [cyan]\\[/cyan] at end of line     — continue typing on the next line
"""


# ── Main ──────────────────────────────────────────────────────────────────────

def start_terminal_chat(agent) -> list:
    if not RICH_AVAILABLE:
        return _plain_chat(agent)

    console = Console()
    history: list[dict] = []
    msg_count = 0

    tool_list = ", ".join(agent.tools) if agent.tools else "none"
    header = Text.assemble(
        ("  ", ""),
        (agent.name, "bold white"),
        ("  ·  tools: ", STYLE_META),
        (tool_list, f"italic {STYLE_META}"),
        ("  ·  started ", STYLE_META),
        (_now(), STYLE_TIMESTAMP),
        ("  ", ""),
    )
    console.print(Panel(header, box=box.DOUBLE_EDGE, style="bold blue", padding=(0, 1)))
    console.print(f"  [dim]Type [bold]help[/bold] for commands · "
                  f"[bold]\\\\[/bold] at line end for multi-line input[/dim]\n")

    while True:

        # ── Input ─────────────────────────────────────────────────────────────
        try:
            first_line = console.input(
                f"[{STYLE_USER}]You[/] [{STYLE_TIMESTAMP}]({_now()})[/]: "
            )
        except (KeyboardInterrupt, EOFError):
            console.print(f"\n[{STYLE_SYSTEM}]Session ended.[/]")
            break

        lines = [first_line]
        while lines[-1].endswith("\\"):
            lines[-1] = lines[-1][:-1]
            try:
                lines.append(console.input(f"[{STYLE_META}]  ...[/] "))
            except (KeyboardInterrupt, EOFError):
                break
        user_input = "\n".join(lines).strip()

        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd in ("exit", "quit", "e", "q"):
            console.print(f"[{STYLE_SYSTEM}]Ending conversation…[/]")
            break

        if cmd == "clear":
            agent.clear_memory()
            history.clear()
            msg_count = 0
            continue

        if cmd == "help":
            console.print(Panel(HELP_TEXT, title="Help", border_style="dim blue"))
            continue

        if cmd == "history":
            if not history:
                console.print(f"[{STYLE_SYSTEM}]No messages yet.[/]")
            for entry in history:
                console.print(f"[{STYLE_META}][{entry['ts']}][/] [{STYLE_USER}]You:[/] {entry['user']}")
                console.print(f"[{STYLE_META}]      [/] [{STYLE_AGENT}]{agent.name}:[/] {entry['agent']}\n")
            continue

        # ── Run agent synchronously ───────────────────────────────────────────
        capture = _StreamCapture()
        response: Optional[str] = None
        error: Optional[Exception] = None

        old_stdout = sys.stdout
        sys.stdout = capture
        start = time.perf_counter()
        try:
            response = agent.run(user_input)
        except Exception as exc:
            error = exc
        finally:
            sys.stdout = old_stdout      # always restore
        elapsed = time.perf_counter() - start

        # ── Output ────────────────────────────────────────────────────────────
        if error:
            console.print(Panel(
                f"[{STYLE_ERROR}]{error}[/]",
                title=f"[{STYLE_ERROR}]Error[/]",
                border_style="red",
            ))
            continue

        msg_count += 1
        trace_lines = capture.get_lines()
        _render_trace(console, trace_lines)

        try:
            body = Markdown(response)
        except Exception:
            body = Text(response)

        meta = (
            f"[{STYLE_TIMESTAMP}]{_now()}  ·  "
            f"{elapsed:.1f}s  ·  "
            f"{_word_count(response)}w  ·  "
            f"msg #{msg_count}[/]"
        )
        console.print(Panel(
            body,
            title=f"[{STYLE_AGENT}]{agent.name}[/]",
            subtitle=meta,
            border_style="green",
            padding=(0, 1),
        ))

        history.append({
            "ts":      _now(),
            "user":    user_input,
            "agent":   response,
            "elapsed": round(elapsed, 2),
            "loops":   len([l for l in trace_lines if "Loop" in l]),
        })

    # ── Session summary ───────────────────────────────────────────────────────
    if history:
        total = sum(e.get("elapsed", 0) for e in history)
        avg_loops = sum(e.get("loops", 0) for e in history) / len(history)
        console.print(Rule(style="dim blue"))
        console.print(
            f"[{STYLE_META}]Session · "
            f"{len(history)} exchange(s) · "
            f"avg {total / len(history):.1f}s · "
            f"avg loops {avg_loops:.1f}[/]\n"
        )

    return history
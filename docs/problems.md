I'll do a thorough, file-by-file review and then give you a prioritized improvement plan.

---

## Critical Bugs First

### Bug 1: `BaseTool.__init__` swallows `abstractmethod`

```python
# CURRENT (broken)
class BaseTool(ABC):
    def __init__(self):
        name: str
        description: str
        parameters: dict = {}

        @abstractmethod          # ← nested INSIDE __init__, never enforced
        def run(self, parameters: dict) -> str:
            pass
```

`run()` is defined **inside** `__init__`. Python never sees it as an abstract method. Any subclass that forgets to implement `run()` will **not** raise `TypeError`. The entire abstraction contract is silently broken.

```python
# FIXED
from abc import ABC, abstractmethod

class BaseTool(ABC):
    name: str = ""
    description: str = ""
    parameters: dict = {}

    @abstractmethod
    def run(self, parameters: dict) -> str:
        """The method called by the agent to run a tool"""
        pass

    def get_schema(self) -> str:
        params_xml = ""
        for param_name, param_desc in self.parameters.items():
            params_xml += f"\n        <{param_name}>({param_desc})</{param_name}>"
        return (
            f"<tool>\n"
            f"  <tool_name>{self.name}</tool_name>\n"
            f"  <description>{self.description}</description>\n"
            f"  <parameters>{params_xml}\n  </parameters>\n"
            f"</tool>"
        )
```

---

### Bug 2: `eval()` in `CalculatorTool` is a security hole

```python
# CURRENT (dangerous)
result = eval(expression)  # eval("__import__('os').system('rm -rf /')") works fine
```

`eval()` executes **any** Python code. If the LLM hallucinates or is prompted maliciously, this destroys files, leaks keys, or worse.

```python
# FIXED - use ast.literal_eval for simple cases, or a safe parser
import ast
import operator

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    parameters = {
        "expression": "The math expression to evaluate. Example: 150*4"
    }

    # Whitelist of safe operations
    _SAFE_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
    }

    def _safe_eval(self, node):
        if isinstance(node, ast.Constant):          # numbers
            return node.value
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in self._SAFE_OPS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            left = self._safe_eval(node.left)
            right = self._safe_eval(node.right)
            return self._SAFE_OPS[op_type](left, right)
        elif isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in self._SAFE_OPS:
                raise ValueError(f"Unsupported operator: {op_type.__name__}")
            return self._SAFE_OPS[op_type](self._safe_eval(node.operand))
        else:
            raise ValueError(f"Unsupported expression type: {type(node).__name__}")

    def run(self, parameters: dict) -> str:
        try:
            expression = parameters.get("expression", "")
            expression = expression.strip().rstrip("=").strip()
            tree = ast.parse(expression, mode="eval")
            result = self._safe_eval(tree.body)
            return str(result)
        except ZeroDivisionError:
            return "Calculator error: Division by zero."
        except ValueError as e:
            return f"Calculator error: {e}"
        except Exception as e:
            return f"Calculator error: {e}"
```

---

### Bug 3: `FileWriterTool` has no path traversal protection

```python
# CURRENT - agent can write to /etc/passwd or ../../secrets.env
with open(filename, "w") as f:
    f.write(content)
```

```python
# FIXED
import os

class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file in the current working directory only."
    parameters = {
        "filename": "The name of the file to write. Example: result.txt",
        "content": "The full text content to write into the file."
    }

    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            content = parameters.get("content", "").strip()

            if not filename:
                return "Error: filename parameter is missing."

            # Prevent path traversal attacks
            safe_path = os.path.realpath(os.path.join(os.getcwd(), filename))
            if not safe_path.startswith(os.getcwd()):
                return "Error: Writing outside the working directory is not allowed."

            # Create subdirectories if needed (safely)
            os.makedirs(os.path.dirname(safe_path), exist_ok=True) \
                if os.path.dirname(safe_path) else None

            with open(safe_path, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"
```

---

### Bug 4: `GeminiClient` uses a non-existent model name

```python
# main.py
llm = GeminiClient(model="gemini-3.1-flash-lite")  # This model does not exist
```

As of 2025, valid model names are `gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-2.0-flash`, etc. This will raise an API error at runtime with a confusing message.

```python
# FIXED geminiclient.py - validate on init
VALID_GEMINI_MODELS = {
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
}

class GeminiClient(BaseLLM):
    def __init__(self, model: str = "gemini-2.0-flash"):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")

        if model not in VALID_GEMINI_MODELS:
            raise ValueError(
                f"Unknown Gemini model: '{model}'. "
                f"Valid options: {sorted(VALID_GEMINI_MODELS)}"
            )

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
```

---

### Bug 5: `LongTermMemory` grows forever and will break the context window

```python
# CURRENT - every single message ever sent gets loaded and sent to LLM
def get_context(self) -> str:
    context = ""
    for entry in self.__history:       # No limit. Session 100 sends 10,000 lines.
        context += f"{entry['role']}: {entry['content']}\n"
    return context
```

After enough sessions, the combined memory exceeds the LLM's context window and the API call fails or gets truncated silently.

```python
# FIXED ltm.py - add a rolling window
class LongTermMemory(BaseMemory):

    def __init__(self, agent_name: str, max_entries: int = 50):
        self.__file_path = f"{agent_name}_memory.json"
        self.__max_entries = max_entries
        self.__history = self.__load_from_file()

    def add_entry(self, role: str, content: str):
        self.__history.append({"role": role, "content": content})
        # Keep only the most recent N entries on disk too
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
        self.__save_to_file()

    def get_context(self) -> str:
        if not self.__history:
            return ""
        # Only send last N entries to LLM to avoid context overflow
        recent = self.__history[-self.__max_entries:]
        return "".join(
            f"{entry['role']}: {entry['content']}\n" for entry in recent
        )
```

---

## Architecture Issues

### Issue 1: `Config` stores `user_prompt` which it never uses

```python
@dataclass
class Config:
    name: str
    description: str = "..."
    system_prompt: str = "You are a helpful AI assistant."
    user_prompt: str = ""        # ← never read by BaseAgent, dead field
    max_tokens: int = 1000       # ← also never used since LLM controls this
```

`user_prompt` belongs to the conversation, not the config. `max_tokens` is already set in `GroqClient`. Remove dead fields.

```python
# FIXED config.py
from dataclasses import dataclass, field

@dataclass
class Config:
    # --- Identity ---
    name: str
    description: str = "A helpful AI agent."

    # --- Prompts ---
    system_prompt: str = "You are a helpful AI assistant."

    # --- Behavior ---
    max_iterations: int = 10

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Agent must have a non-empty name")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than 0")
```

---

### Issue 2: `registry.register()` prints to stdout unconditionally

```python
def register(self, tool: BaseTool):
    self.__tools[tool.name] = tool
    print(f"Registered tool: {tool.name}")   # ← pollutes output in production
```

This is a debug statement left in. In a real system, registration output should be opt-in.

```python
# FIXED registry.py
import logging

logger = logging.getLogger(__name__)

class ToolRegistry:
    def __init__(self):
        self.__tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool):
        if not isinstance(tool, BaseTool):
            raise TypeError(f"Expected BaseTool, got {type(tool).__name__}")
        if not tool.name:
            raise ValueError("Tool must have a non-empty name")
        if tool.name in self.__tools:
            logger.warning(f"Tool '{tool.name}' is being overwritten in registry.")
        self.__tools[tool.name] = tool
        logger.debug(f"Registered tool: {tool.name}")

    def get_tool(self, name: str):
        return self.__tools.get(name)

    def get_descriptions(self) -> str:
        return "\n\n".join(tool.get_schema() for tool in self.__tools.values())

    def list_tools(self) -> list[str]:
        return list(self.__tools.keys())

    def __len__(self) -> int:
        return len(self.__tools)
```

---

### Issue 3: `BaseLLM.generate()` has a redundant `raise NotImplementedError`

```python
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt, user_prompt) -> str:
        raise NotImplementedError    # ← pointless, ABC already enforces this
```

`@abstractmethod` already prevents instantiation. `raise NotImplementedError` is redundant and adds noise. Also, add type hints.

```python
# FIXED basellm.py
from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """
        Send a prompt to the LLM and return the text response.

        Args:
            system_prompt: Instructions that define the agent's behavior.
            user_prompt: The conversation history and current task.

        Returns:
            The LLM's text response.
        """
        pass
```

---

### Issue 4: `chat_ui.py` loses the last response after loop ends

```python
def start_terminal_chat(agent):
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation...")
            break
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
```

And in `main.py`:
```python
start_terminal_chat(agent)
print("\nFinal Answer:")
# print(response)       ← response is undefined here, this would crash
```

The function returns nothing. Make it return the conversation history.

```python
# FIXED chat_ui.py
def start_terminal_chat(agent) -> list[dict]:
    """
    Run an interactive terminal chat session.

    Returns:
        List of conversation turns: [{"user": ..., "agent": ...}, ...]
    """
    print("=" * 50)
    print(f"Chat with {agent.name}  |  Tools: {agent.available_tools}")
    print("Type 'exit' or 'quit' to end. Type 'clear' to reset memory.")
    print("=" * 50)

    history = []

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted.")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Ending conversation...")
            break

        if user_input.lower() == "clear":
            agent.clear_memory()
            print("[Memory cleared]")
            continue

        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
        history.append({"user": user_input, "agent": response})

    return history
```

---

## Code Quality Issues

### Issue 5: `ShortTermMemory` and `LongTermMemory` duplicate `get_context()`

Both classes have this identical method:

```python
def get_context(self) -> str:
    if not self.__history:
        return ""
    context = ""
    for entry in self.__history:
        context += f"{entry['role']}: {entry['content']}\n"
    return context
```

Move the shared logic to `BaseMemory` as a concrete method.

```python
# FIXED memory/memory.py
from abc import ABC, abstractmethod

class BaseMemory(ABC):

    @abstractmethod
    def add_entry(self, role: str, content: str) -> None:
        pass

    @abstractmethod
    def get_history(self) -> list[dict]:
        """Return raw history list for subclasses to implement."""
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    def get_context(self) -> str:
        """Format history as a readable string. Shared by all subclasses."""
        history = self.get_history()
        if not history:
            return ""
        return "".join(
            f"{entry['role']}: {entry['content']}\n" for entry in history
        )
```

```python
# FIXED memory/stm.py
from memory.memory import BaseMemory

class ShortTermMemory(BaseMemory):

    def __init__(self):
        self.__history: list[dict] = []

    def add_entry(self, role: str, content: str) -> None:
        self.__history.append({"role": role, "content": content})

    def get_history(self) -> list[dict]:
        return self.__history.copy()    # Return copy, not the live list

    def clear(self) -> None:
        self.__history = []
```

---

### Issue 6: String concatenation in loops is O(n²)

```python
# CURRENT - inefficient
context = ""
for entry in self.__history:
    context += f"{entry['role']}: {entry['content']}\n"   # new string object each iteration
```

Use `str.join()` instead. It allocates once.

```python
# FIXED - O(n)
return "".join(
    f"{entry['role']}: {entry['content']}\n" for entry in history
)
```

---

### Issue 7: `directory_watcher.py` uses `os.listdir()` which is too shallow

Based on the context description, `os.listdir()` only shows the top level. For an agent working inside a project, it needs a recursive tree view to be useful.

```python
# IMPROVED directory_watcher.py
import os
from tools.basetool import BaseTool

class DirectoryWatcherTool(BaseTool):
    name = "directory_watcher"
    description = "Returns the directory tree of a given path."
    parameters = {
        "path": "The directory path to inspect. Use '.' for current directory.",
        "max_depth": "Maximum depth to recurse. Default is 3."
    }

    def run(self, parameters: dict) -> str:
        try:
            path = parameters.get("path", ".").strip() or "."
            max_depth = int(parameters.get("max_depth", 3))

            if not os.path.exists(path):
                return f"Error: Path '{path}' does not exist."

            lines = []
            self._walk(path, lines, depth=0, max_depth=max_depth)
            return "\n".join(lines) if lines else "Directory is empty."
        except Exception as e:
            return f"Error: {e}"

    def _walk(self, path: str, lines: list, depth: int, max_depth: int):
        if depth > max_depth:
            return
        indent = "  " * depth
        try:
            entries = sorted(os.listdir(path))
        except PermissionError:
            lines.append(f"{indent}[Permission Denied]")
            return
        for entry in entries:
            lines.append(f"{indent}{entry}")
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                self._walk(full_path, lines, depth + 1, max_depth)
```

---

## What to Add Next

### Addition 1: A `WebSearchTool` using DuckDuckGo (no API key needed)

```python
# tools/web_search.py
import urllib.request
import urllib.parse
import json
from tools.basetool import BaseTool

class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Searches the web using DuckDuckGo and returns top results."
    parameters = {
        "query": "The search query. Example: Python asyncio tutorial"
    }

    def run(self, parameters: dict) -> str:
        try:
            query = parameters.get("query", "").strip()
            if not query:
                return "Error: query parameter is missing."

            encoded = urllib.parse.quote(query)
            url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1"

            with urllib.request.urlopen(url, timeout=10) as response:
                data = json.loads(response.read().decode())

            results = []

            if data.get("AbstractText"):
                results.append(f"Summary: {data['AbstractText']}")

            for topic in data.get("RelatedTopics", [])[:5]:
                if "Text" in topic:
                    results.append(f"- {topic['Text']}")

            return "\n".join(results) if results else "No results found."

        except Exception as e:
            return f"Web search error: {e}"
```

---

### Addition 2: Proper logging instead of `print()`

```python
# utils/logger.py
import logging
import sys

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates a configured logger for the framework.

    Usage:
        from utils.logger import setup_logger
        logger = setup_logger(__name__)
        logger.info("Agent started")
        logger.debug("Tool called: calculator")
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s %(name)s: %(message)s",
            datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
```

---

### Addition 3: A `MemorySummarizationTool` to prevent context overflow

```python
# memory/summarizer.py
class MemorySummarizer:
    """
    Uses the agent's own LLM to compress long memory into a short summary.
    Call this when get_context() exceeds a token threshold.
    """

    def __init__(self, llm):
        self.llm = llm

    def summarize(self, context: str) -> str:
        system = "You are a memory compression assistant."
        user = (
            f"Compress the following conversation history into a concise summary "
            f"that preserves all important facts, decisions, and tool results:\n\n"
            f"{context}"
        )
        try:
            return self.llm.generate(system, user)
        except Exception as e:
            return f"[Summary failed: {e}]\n{context[-500:]}"  # fallback to tail
```

---

## Complete Priority List

```
PRIORITY 1 - Fix Before Using (Bugs)
─────────────────────────────────────
[ ] Fix BaseTool: move @abstractmethod outside __init__
[ ] Replace eval() in CalculatorTool with ast-based safe parser
[ ] Add path traversal protection to FileWriterTool
[ ] Fix GeminiClient model name (gemini-3.1-flash-lite does not exist)
[ ] Add LongTermMemory rolling window to prevent context overflow

PRIORITY 2 - Architecture Cleanup
───────────────────────────────────
[ ] Remove dead fields from Config (user_prompt, max_tokens)
[ ] Remove print() from ToolRegistry.register(), use logging
[ ] Add duplicate tool name warning in ToolRegistry
[ ] Move shared get_context() to BaseMemory base class
[ ] Remove redundant raise NotImplementedError from BaseLLM
[ ] Make chat_ui return conversation history

PRIORITY 3 - Code Quality
──────────────────────────
[ ] Replace string concatenation loops with str.join()
[ ] Add type hints to all method signatures
[ ] Add docstrings to all public methods
[ ] Return copies not live lists from ShortTermMemory
[ ] Make DirectoryWatcherTool recursive with max_depth

PRIORITY 4 - New Features
──────────────────────────
[ ] Add WebSearchTool (DuckDuckGo, no key needed)
[ ] Add proper logging module (utils/logger.py)
[ ] Add MemorySummarizer to handle context overflow gracefully
[ ] Add SupervisorAgent that routes tasks between specialized agents
[ ] Add tests/ directory with at least unit tests for each tool
```

The most important fix by far is **Bug 1** (the `BaseTool` abstract method placement). Your entire tool safety net is currently non-functional because of it, and you would not know until a tool silently misbehaved.\\\




im not gonna fix bug 2 for a while were going to focus on other imp stuff for now
bug 4 seems to be unecessary to fix cuz right now im the only user
also add a list of models feels a lot of work for providers like openrouter and cerebras that keep changing models everyday

lets focus on the logterm memory and also fix the memory once and for all
im open to anyu type of suggestions
and we can also add the episoidic memory
also i want to hear about more better memory if possible cuz what i have been using uptil now is just the ancients just in  order to learn stuff and im still incistant on learning things thats why im developing this shit framework from scratch
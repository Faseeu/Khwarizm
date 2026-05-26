## File: `agents/__init__.py`
<file path="agents/__init__.py" type="python">
```python

```
</file>
## File: `agents/baseagent.py`
<file path="agents/baseagent.py" type="python">
```python
from agents.config import Config
from llms import BaseLLM
from tools import ToolRegistry
from memory.stm import ShortTermMemory
from memory.ltm import LongTermMemory
import xml.etree.ElementTree as ET
class BaseAgent:
    def __init__(self,
                name,
                llm:BaseLLM,
                system_prompt: str = "You are a helpful AI assistant", 
                tools: list = None
                ):
        self.llm = llm
        self.registry = ToolRegistry()
        tools = tools or []
        # THE LOOP 
        # Which automates the work of resgistering the TOOLS manually
        for tool in tools:
            self.registry.register(tool)
        # This is basically a prompt that tells the llm what tools it has
        if tools:
            tool_schemas = self.registry.get_descriptions()
            system_prompt = (
                f"{system_prompt}\n\n"
                f"You have access to these tools:\n"
                f"{tool_schemas}\n\n"
                f"STRICT RULES:\n"
                f"CRITICAL: Only use ONE tool per response. Wait for the tool result before taking your next step.\n"
                f"1. Use ONE tool per response. No exceptions.\n"
                f"2. After using a tool,Stop. wait for the result before continuing. Do not write anything else.\n"
                f"3. If you use more than one tool in a single response, I will stop the conversation and you will fail the task.\n\n"
                f"4. NEVER call the same or different tool twice in one response.\n"
                f"5. You MUST use tools when the task requires them.\n\n"
                f"To use a tool, respond EXACTLY in this XML format:\n\n"
                f"<tool_use>\n"
                f"  <tool_name>tool_name_here</tool_name>\n"
                f"  <parameters>\n"
                f"    <param_name>value here</param_name>\n"
                f"  </parameters>\n"
                f"</tool_use>"
            )
        # THE CONFIG
        self.config = Config(
            name=name,
            description="Agent",
            system_prompt=system_prompt,
        )
        # Memory 
        # The Memory part of the agent
        # Truly automatic  
        self.__base_system_prompt = system_prompt
        self.__short_term = ShortTermMemory(max_entries=self.config.max_stm_entries)
        self.__long_term = LongTermMemory(
            agent_name=name,
            max_entries=self.config.max_ltm_entries
            )
    @property
    def name(self) -> str:
        # agent's name
        return self.config.name
    @property
    def description(self) -> str:
        # agent's description
        return self.config.description
    @property
    def system_prompt(self) -> str:
        # system prompt
        return self.config.system_prompt
    @property
    def tools(self) -> list:
        # list of tool names
        return self.registry.list_tools()
    def run(self, user_input: str) -> str:
        self.__short_term.add_entry(role="user", content= user_input)
        self.__long_term.add_entry(role="user", content= user_input)
        iterations = 0
        max_iters = self.config.max_iterations
        print(f"Starting: {self.config.name} \n{self.config.name} is thinking...")
        while iterations < max_iters:
            iterations += 1
            print(f"  [Loop {iterations}/{max_iters}] Agent is thinking...")
            #  Build context from BOTH memories
            long_term_context = self.__long_term.get_context()
            short_term_context = self.__short_term.get_context()
            #  Combine them into one prompt
            full_context = (
                f"Past Conversations:\n{long_term_context}\n\n"
                f"Current Session:\n{short_term_context}"
            )
            # print("\n--- SYSTEM PROMPT ---")
            # print(self.config.system_prompt)
            # print("--- END SYSTEM PROMPT ---\n")
            response = self.llm.generate(
                system_prompt=self.__base_system_prompt,
                user_prompt=full_context
            )
            if response.startswith("Error: LLM API failed"):
                print("  -> Critical LLM Error encountered.")
                return response
            if "<think>" in response and "</think>" in response:
                response = response.split("</think>")[-1].strip()
        # Check if LLM decided to use a tool
            if "<tool_use>" in response:
                tool_note = self.__handle_tool_call(response)
                self.__short_term.add_entry(
                    role="assistant",
                    content=response
                )
                self.__short_term.add_entry(
                    role="tool",
                    content=tool_note
                )
                continue
             # Save to both memories
            self.__short_term.add_entry(role="assistant", content=response)
            self.__long_term.add_entry(role="assistant", content=response)
            return response if response else "Error: Agent reached max iterations without a final answer."
    def __handle_tool_call(self, response: str) -> str:
        try:
            start = response.find("<tool_use>")
            end = response.find("</tool_use>") + len("</tool_use>")
            xml_block = response[start:end]
            root = ET.fromstring(xml_block)
            # Extract tool name
            tool_name_el = root.find("tool_name")
            if tool_name_el is None:
                return "Error: No tool_name found in XML."
            tool_name = tool_name_el.text.strip()
            parameters = {}
            params_el = root.find("parameters")
            if params_el is not None:
                for param in params_el:
                    parameters[param.tag] = param.text.strip() if param.text else ""
            print(f"  -> Tool: {tool_name} | Parameters: {parameters}")
            # Fetch the tool from registry
            tool = self.registry.get_tool(tool_name)
            if not tool:
                return f"Error: Unknown tool '{tool_name}'. Available: {self.registry.list_tools()}"
            # Run the tool with the clean dictionary
            result = tool.run(parameters)
            return f"Tool '{tool_name}' returned: {result}"
        except ET.ParseError as e:
            return f"Error: Could not parse XML tool call. Details: {e}"
        except Exception as e:
            return f"Error during tool execution: {e}"
    def clear_memory(self):
        self.__short_term.clear()
        self.__long_term.clear()
        print(f"[{self.name}] Memory cleared.")
```
</file>
## File: `agents/config.py`
<file path="agents/config.py" type="python">
```python
from dataclasses import dataclass
@dataclass
class Config:
#---Identity
    name: str
    # model: str
    description: str = "This AI agent is like an AI from the future and will give you futuristic explainations for every question you ask."
#---Prompts
    system_prompt: str = "You are a helpful AI assistant."
#---LLM Settings
    max_tokens: int = 1000
#---Behavior settings
    max_iterations: int = 50
     # --- Memory ---
    max_ltm_entries: int = 100
    max_stm_entries: int = 50
    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Agent must have a name")
        if self.max_tokens <= 0:
            raise ValueError("max_tokens must be greater than 0")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than 0")
        if self.max_ltm_entries <= 0:
            raise ValueError("max_ltm_entries must be greater than 0")
        if self.max_stm_entries <= 0:
            raise ValueError("max_stm_entries must be greater than 0")
```
</file>
## File: `llms/__init__.py`
<file path="llms/__init__.py" type="python">
```python
from .basellm import BaseLLM
from .groqclient import GroqClient
```
</file>
## File: `llms/basellm.py`
<file path="llms/basellm.py" type="python">
```python
from abc import ABC , abstractmethod
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt, user_prompt) ->str:
        pass
```
</file>
## File: `llms/geminiclient.py`
<file path="llms/geminiclient.py" type="python">
```python
import os
import google.generativeai as genai
from llms.basellm import BaseLLM
class GeminiClient(BaseLLM):
    def __init__(self, model: str = "gemini-1.5-flash"):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")
        # Configure Google's SDK
        genai.configure(api_key=api_key)
        # Initialize the model
        self.model = genai.GenerativeModel(model)
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            full_prompt = f"System Instructions:\n{system_prompt}\n\nUser Input:\n{user_prompt}"
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error: Gemini API failed with message: {str(e)}"
```
</file>
## File: `llms/groqclient.py`
<file path="llms/groqclient.py" type="python">
```python
from llms.basellm import BaseLLM
from groq import Groq
class GroqClient(BaseLLM):
    def __init__(self, model: str, max_tokens: int = 1000 ):
        self.client = Groq()
        self.model = model
        self.max_tokens = max_tokens
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens = self.max_tokens,
                messages = [
                    {"role": "system", "content" : system_prompt},
                    {"role": "user" , "content" : user_prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: LLM API failed with message: {str(e)}"
```
</file>
## File: `memory/__init__.py`
<file path="memory/__init__.py" type="python">
```python

```
</file>
## File: `memory/ltm.py`
<file path="memory/ltm.py" type="python">
```python
import json
import os
from memory.memory import BaseMemory
class LongTermMemory(BaseMemory):
    def __init__(self, agent_name: str, max_entries: int = 100):
        self.__file_path = f"{agent_name}_memory.json"
        self.__max_entries = max_entries
        self.__history = self.__load_from_file()
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
        self.__save_to_file()
    def get_context(self) -> str:
        if not self.__history:
            return ""
        return "".join([
            f"{entry['role']}: {entry['content']}\n"
        for entry in self.__history
        ])
    def clear(self):
        self.__history = []
        self.__save_to_file()
    def __save_to_file(self):
        try:
            with open(self.__file_path, "w") as f:
                json.dump(self.__history, f, indent=4)
        except Exception as e:
            print(f"Warning: Could not save memory to {self.__file_path}. Error: {e}")
    def __load_from_file(self) -> list:
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Memory file corrupted or unreadable. Starting fresh. Error: {e}")
                return []
        return []
```
</file>
## File: `memory/memory.py`
<file path="memory/memory.py" type="python">
```python
from abc import ABC, abstractmethod
class BaseMemory(ABC):
    @abstractmethod
    def add_entry(self, role: str, content: str):
        """Save a new message to memory"""
        pass
    @abstractmethod
    def get_context(self) -> str:
        """Retrieve full history as a string for the LLM"""
        pass
    @abstractmethod
    def clear(self):
        """Reset memory completely"""
        pass
#Roles: The talking entities in a conversation
# user, assistant, system
#  ShortTerm memory: Just a list having the messages #
```
</file>
## File: `memory/stm.py`
<file path="memory/stm.py" type="python">
```python
from memory.memory import BaseMemory
class ShortTermMemory(BaseMemory):
    def __init__(self, max_entries=50):
        self.__history = []
        self.__max_entries = max_entries
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })
        if len(self.__history) > self.__max_entries:
            self.__history = self.__history[-self.__max_entries:]
    def get_context(self) -> str:
        if not self.__history:
            return ""
        context = ""
        for entry in self.__history:
            context += f"{entry['role']}: {entry['content']}\n"
        return context
    def clear(self):
        self.__history = []
```
</file>
## File: `tools/agent_made/__init__.py`
<file path="tools/agent_made/__init__.py" type="python">
```python

```
</file>
## File: `tools/agent_made/directory_watcher.py`
<file path="tools/agent_made/directory_watcher.py" type="python">
```python
from tools.basetool import BaseTool
import os
class DirectoryWatcherTool(BaseTool):
    def __init__(self):
        self.name = "directory_watcher"
        self.description = "Lists files in a directory to keep track of changes."
        self.parameters = {
            "path": "The path of the directory to list."
        }
    def run(self, parameters: dict) -> str:
        path = parameters.get("path", ".")
        try:
            files = os.listdir(path)
            return f"Files in {path}: {', '.join(files)}"
        except Exception as e:
            return f"Error accessing directory: {str(e)}"
```
</file>
## File: `tools/agent_made/git_manager.py`
<file path="tools/agent_made/git_manager.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess
class GitManagerTool(BaseTool):
    def __init__(self):
        self.name = "git_manager"
        self.description = "Provides a safe interface to run 'git status' or 'git log' to track project changes."
        self.parameters = {
            "command": "The git command to execute (e.g., 'status', 'log -n 5')."
        }
    def run(self, parameters: dict) -> str:
        cmd_arg = parameters.get("command", "status")
        full_command = f"git {cmd_arg}"
        print(f"The following git command will be executed: {full_command}. Proceed? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            try:
                result = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Git command failed: {e.output}"
        else:
            return "Git command execution cancelled by user."
```
</file>
## File: `tools/agent_made/light_python_runner.py`
<file path="tools/agent_made/light_python_runner.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess
import os
import shutil
class LightPythonRunnerTool(BaseTool):
    def __init__(self):
        self.name = "light_python_runner"
        self.description = "Executes python files in a clean, ephemeral virtual environment that is deleted immediately after execution."
        self.parameters = {
            "filepath": "The path to the python file to execute."
        }
    def run(self, parameters: dict) -> str:
        filepath = parameters.get("filepath", "")
        venv_dir = ".ephemeral_venv"
        # Cleanup if old one exists
        if os.path.exists(venv_dir):
            shutil.rmtree(venv_dir)
        cmd = f"python3 -m venv {venv_dir} && {venv_dir}/bin/python3 {filepath}"
        print(f"The following ephemeral python execution will be run: {cmd}. Proceed? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            try:
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Execution failed: {e.output}"
            finally:
                if os.path.exists(venv_dir):
                    shutil.rmtree(venv_dir)
        else:
            return "Execution cancelled by user."
```
</file>
## File: `tools/agent_made/terminal_executor.py`
<file path="tools/agent_made/terminal_executor.py" type="python">
```python
from tools.basetool import BaseTool
import subprocess
class TerminalExecutorTool(BaseTool):
    def __init__(self):
        self.name = "terminal_executor"
        self.description = "Executes shell commands after explicit user confirmation."
        self.parameters = {
            "command": "The shell command to be executed."
        }
    def run(self, parameters: dict) -> str:
        command = parameters.get("command", "")
        print(f"The following command will be executed: {command}. Proceed? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Command failed: {e.output}"
        else:
            return "Command execution cancelled by user."
```
</file>
## File: `tools/__init__.py`
<file path="tools/__init__.py" type="python">
```python
from tools.basetool import BaseTool
from tools.calculator import CalculatorTool
from tools.registry import ToolRegistry
from tools.filereader import FileReaderTool
from tools.filewriter import FileWriterTool
```
</file>
## File: `tools/basetool.py`
<file path="tools/basetool.py" type="python">
```python
from abc import ABC,abstractmethod
class BaseTool(ABC):
    def __init__(self):
        name: str
        description: str
        parameters: dict={}
    @abstractmethod
    def run(self, parameters: dict) -> str:
        """The method called by the agent to run a tool"""
        pass
    def get_schema(self) -> str:
        """Builds the XML schema shown to the LLM"""
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
</file>
## File: `tools/calculator.py`
<file path="tools/calculator.py" type="python">
```python
from tools.basetool import BaseTool
class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Evaluates a mathematical expression and returns the result."
    parameters = {
        "expression": "The math expression to evaluate. Example: 150*4"
    }
    def run(self, parameters: dict) -> str:
        try:
            expression = parameters.get("expression", "")
            # Clean any trailing = signs the LLM might add
            expression = expression.strip().rstrip("=").strip()
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Calculator error: {e}"
```
</file>
## File: `tools/filereader.py`
<file path="tools/filereader.py" type="python">
```python
from tools.basetool import BaseTool
class FileReaderTool(BaseTool):
    name = "file_reader"
    description = "Reads and returns the content of a file."
    parameters = {
        "filename": "The name of the file to read. Example: result.txt"
    }
    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            if not filename:
                return "Error: filename parameter is missing."
            with open(filename, "r") as f:
                content = f.read()
            return f"Content of {filename}:\n{content}"
        except FileNotFoundError:
            return f"Error: File '{filename}' not found."
        except Exception as e:
            return f"Error reading file: {e}"
```
</file>
## File: `tools/filewriter.py`
<file path="tools/filewriter.py" type="python">
```python
from tools.basetool import BaseTool
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
</file>
## File: `tools/registry.py`
<file path="tools/registry.py" type="python">
```python
from tools.basetool import BaseTool
class ToolRegistry:
    def __init__(self):
        self.__tools = {}
    def register(self, tool: BaseTool):
        self.__tools[tool.name] = tool
        print(f"Registered tool: {tool.name}")
    def get_tool(self, name: str) -> BaseTool:
        return self.__tools.get(name)
    def get_descriptions(self) -> str:
        """Returns full XML schemas for all tools"""
        schemas = []
        for tool in self.__tools.values():
            schemas.append(tool.get_schema())
        return "\n\n".join(schemas)
    def list_tools(self) -> list:
        return list(self.__tools.keys())
```
</file>
## File: `tools/s.txt`
<file path="tools/s.txt" type="text">
```text
git config --global user.email "faseuu@gmail.com"
git config --global user.name "Faseeu"
```
</file>
## File: `utils/chat_ui.py`
<file path="utils/chat_ui.py" type="python">
```python
# utils/chat_ui.py
def start_terminal_chat(agent):
    print("=" * 50)
    print(f"Starting chat with {agent.name}. Type 'exit' to quit.")
    print("=" * 50)
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation...")
            break
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
```
</file>
## File: `__init__.py`
<file path="__init__.py" type="python">
```python

```
</file>
## File: `generate_codecontext.py`
<file path="generate_codecontext.py" type="python">
```python
import datetime
from pathlib import Path
from typing import Dict, List, Set
def generate_context() -> None:
    output_file = Path("codecontext.md")
    project_root = Path(".")
    # --- CONFIGURATION & SAFETY SAFETY VALVES ---
    MAX_FILE_SIZE_BYTES = 200 * 1024  # 200 KB individual file ceiling guard
    ignore_dirs: Set[str] = {
        '__pycache__', 'tests', 'venv', '.venv', '.git', 
        '.env', '.ephemeral_venv', '.temp_venv', '.idea', '.vscode'
    }
    ignore_files: Set[str] = {
        'codecontext.md',
        'context.md',
        'Agent1_memory.json'
    }
    allowed_extensions: Set[str] = {'.py', '.md', '.txt', '.html', '.yaml', '.yml'}
    lang_mapping: Dict[str, str] = {
        '.py': 'python', '.html': 'html', '.md': 'markdown',
        '.json': 'json', '.yaml': 'yaml', '.yml': 'yaml'
    }
    # Reporting Metrics
    total_files_scanned = 0
    total_lines_scanned = 0
    truncated_files_count = 0
    tree_lines: List[str] = ["# Project Architecture\n\n```text\n"]
    context_lines: List[str] = ["\n# Source Code Deep-Dive\n\n"]
    # --- RECURSIVE ENGINE WITH TIMESTAMPS & SIZE CHECKS ---
    def build_tree(dir_path: Path, prefix: str = "") -> None:
        nonlocal total_files_scanned, total_lines_scanned, truncated_files_count
        try:
            entries = sorted(
                [e for e in dir_path.iterdir() if e.name not in ignore_dirs and not e.name.startswith('.')],
                key=lambda e: (e.is_file(), e.name.lower())
            )
        except PermissionError:
            return
        for i, entry in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = "└── " if is_last else "├── "
            # Fetch last modified timestamp dynamically
            mtime = entry.stat().st_mtime
            timestamp = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
            if entry.is_dir():
                tree_lines.append(f"{prefix}{connector}{entry.name}/ [{timestamp}]\n")
                next_prefix = prefix + ("    " if is_last else "│   ")
                build_tree(entry, next_prefix)
            elif entry.is_file():
                file_size_kb = entry.stat().st_size / 1024
                tree_lines.append(f"{prefix}{connector}{entry.name} ({file_size_kb:.1f} KB) [{timestamp}]\n")
                # Content Processing Block
                if entry.suffix in allowed_extensions and entry.name not in ignore_files:
                    total_files_scanned += 1
                    lang = lang_mapping.get(entry.suffix, 'text')
                    # Structural Markdown Title
                    context_lines.append(f"## File: `{entry.as_posix()}`\n")
                    context_lines.append(f"**Last Modified:** `{timestamp}` | **Size:** `{file_size_kb:.2f} KB`\n\n")
                    # AI-Directives: XML opening anchor tags for crisp context parsing
                    context_lines.append(f'<file path="{entry.as_posix()}" type="{lang}">\n```{lang}\n')
                    # Enforce Maximum File Size Limit Guard
                    if entry.stat().st_size > MAX_FILE_SIZE_BYTES:
                        context_lines.append(f"// [SYSTEM WARNING: File content truncated. Exceeds safely limit of {MAX_FILE_SIZE_BYTES // 1024} KB]\n")
                        truncated_files_count += 1
                    else:
                        try:
                            content = entry.read_text(encoding="utf-8")
                            total_lines_scanned += len(content.splitlines())
                            context_lines.append(content)
                        except Exception as e:
                            context_lines.append(f"// Error reading file contents: {e}")
                    # AI-Directives: XML closing tags
                    context_lines.append(f'\n```\n</file>\n\n---\n\n')
    # Run the builder
    root_timestamp = datetime.datetime.fromtimestamp(project_root.resolve().stat().st_mtime).strftime('%Y-%m-%d %H:%M')
    tree_lines.append(f"{project_root.resolve().name}/ [{root_timestamp}]\n")
    build_tree(project_root)
    tree_lines.append("```\n")
    # --- SUMMARY DASHBOARD GENERATION ---
    summary_header = (
        f"# System Context Report\n\n"
        f"| Metric | Status / Value |\n"
        f"| :--- | :--- |\n"
        f"| **Scanned Files** | {total_files_scanned} source targets |\n"
        f"| **Total Lines Parsed** | {total_lines_scanned} lines processed |\n"
        f"| **Truncated Safety Alerts** | {truncated_files_count} files skipped |\n"
        f"| **Target Environment** | Minimalist Agent Framework (Khwarizm) |\n\n"
        f"---\n\n"
    )
    # Fast Single-Pass RAM Array compilation to Disk
    full_payload = summary_header + "".join(tree_lines + context_lines)
    output_file.write_text(full_payload, encoding="utf-8")
    print(f"🚀 Context completely mapped into {output_file} | Total Lines: {total_lines_scanned} | Truncated: {truncated_files_count}")
if __name__ == "__main__":
    generate_context()
```
</file>
## File: `main.py`
<file path="main.py" type="python">
```python
# from llms.groqclient import GroqClient
# from llms.geminiclient import GeminiClient
# from tools.calculator import CalculatorTool
# from tools.filewriter import FileWriterTool
# from tools.filereader import FileReaderTool
# from agents.baseagent import BaseAgent
from utils.chat_ui import start_terminal_chat
# if __name__ == "__main__":
#     # 1. Create the LLM
#     groq_llm = GroqClient(model="llama-3.3-70b-versatile")
#     # 2. Create the Agent with tools
#     agent = BaseAgent(
#         name="SmartBot",
#         llm=gemini_llm,
#         system_prompt= """
#         Be a helpful assistant who always always uses the tools given to him. 
#         Never do a task without using the apppropriate tools. 
#         You have all the appropriate tools at your disposal to perfrom the tasks i ask of you.
#         Always try to reason everything yourself.
#         Try your best not to bother user.
#         Create plans to perform the tasks.
#         Also at the end of each task try to double check if it was properly fullfilled or not. 
#         """,
#         tools=[CalculatorTool(),FileReaderTool(),FileWriterTool()]
#     )
#     print("\n" + "=" * 40)
#     print("TEST 2: Tool needed")
#     print("=" * 40)
# #     response2 = agent.run("""
# #     🌀 SYSTEM OVERRIDE: PROJECT HIDDEN GEM 🌀
# # Agent, your framework is entering the **Anime Recommendation Gauntlet**.  
# # Your mission: populate three classified dossiers, then unleash a fourth wild-card category that breaks the genre matrix.
# # ---
# # 📁 DOSSIER 1: `action`  
# # Compile the absolute GOATed action anime—titles with timelines so beautifully convoluted they require a whiteboard, and stories that hit harder than a final-form scream. Save the list to a file named **`action`**.
# # 📁 DOSSIER 2: `psychological`  
# # Infiltrate the deep cuts. I need **5 criminally underrated psychological anime** that are:
# # - Motivational enough to make me run through a wall,
# # - Political enough to start a debate club,
# # - Obscure enough that even seasoned weebs reply, *"Never heard of it."*  
# # Drop these into **`psychological`**.
# # 📁 DOSSIER 3: `most motivational anime`  
# # Uncover **5 motivational masterpieces** flying completely under the radar. Not the mainstream hype trains—actual underground bangers that rebuild your soul episode by episode. Write these to **`most motivational anime`**.
# # 🎲 DOSSIER 4: `[REDACTED]`  
# # Finally, deploy the wildcard. Create **one additional file** with a category so specific, so dangerously niche, that it feels like it was tailor-made for my brain. Make me fall in love with something I didn’t know existed.
# # ---
# # Execute with maximum flair. Framework stress-test: **ACTIVE**. ⚡
# #     """)
# #     print(response2)
#     start_terminal_chat(agent)
#     # # TEST THE PROPERTIES:
#     # print("--- AGENT INFO ---")
#     # print(f"Name: {agent.name}")                
#     # print(f"Tools: {agent.tools}")     
#     # print(f"Prompt: {agent.system_prompt}")      
#     # print("------------------")
from llms.geminiclient import GeminiClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
from tools.agent_made.terminal_executor import TerminalExecutorTool
if __name__ == "__main__":
    llm = GeminiClient(model="gemini-3.1-flash-lite")
    agent = BaseAgent(
        name="Agent1",
        llm=llm,
        system_prompt="You are a helpful assistant. Always use tools for math and files. Always use tools. Never try to solve any math eq internally",
        tools=[CalculatorTool(), FileWriterTool(), FileReaderTool(),TerminalExecutorTool()]
    )
    # Test multi-parameter tool call
    # response = agent.run("""
    # Study the whole of tools directory
    # and create for yourself a terminal usage tool 
    # but it should have feature to show to the user
    # what command is going to be ran 
    # and ask him yes for y and no for n
    # """)
    start_terminal_chat(agent)
    print("\nFinal Answer:")
    # print(response)
        # "Calculate 1234 multiplied by 5678. "
        # "Then save the result to a file called answer.txt. "
        # "Then read the file back."
```
</file>
## File: `main2.py`
<file path="main2.py" type="python">
```python
# from llms.groqclient import GroqClient
# from llms.geminiclient import GeminiClient
# from tools.calculator import CalculatorTool
# from tools.filewriter import FileWriterTool
# from tools.filereader import FileReaderTool
# from agents.baseagent import BaseAgent
from utils.chat_ui import start_terminal_chat
# if __name__ == "__main__":
#     # 1. Create the LLM
#     groq_llm = GroqClient(model="llama-3.3-70b-versatile")
#     # 2. Create the Agent with tools
#     agent = BaseAgent(
#         name="SmartBot",
#         llm=gemini_llm,
#         system_prompt= """
#         Be a helpful assistant who always always uses the tools given to him. 
#         Never do a task without using the apppropriate tools. 
#         You have all the appropriate tools at your disposal to perfrom the tasks i ask of you.
#         Always try to reason everything yourself.
#         Try your best not to bother user.
#         Create plans to perform the tasks.
#         Also at the end of each task try to double check if it was properly fullfilled or not. 
#         """,
#         tools=[CalculatorTool(),FileReaderTool(),FileWriterTool()]
#     )
#     print("\n" + "=" * 40)
#     print("TEST 2: Tool needed")
#     print("=" * 40)
# #     response2 = agent.run("""
# #     🌀 SYSTEM OVERRIDE: PROJECT HIDDEN GEM 🌀
# # Agent, your framework is entering the **Anime Recommendation Gauntlet**.  
# # Your mission: populate three classified dossiers, then unleash a fourth wild-card category that breaks the genre matrix.
# # ---
# # 📁 DOSSIER 1: `action`  
# # Compile the absolute GOATed action anime—titles with timelines so beautifully convoluted they require a whiteboard, and stories that hit harder than a final-form scream. Save the list to a file named **`action`**.
# # 📁 DOSSIER 2: `psychological`  
# # Infiltrate the deep cuts. I need **5 criminally underrated psychological anime** that are:
# # - Motivational enough to make me run through a wall,
# # - Political enough to start a debate club,
# # - Obscure enough that even seasoned weebs reply, *"Never heard of it."*  
# # Drop these into **`psychological`**.
# # 📁 DOSSIER 3: `most motivational anime`  
# # Uncover **5 motivational masterpieces** flying completely under the radar. Not the mainstream hype trains—actual underground bangers that rebuild your soul episode by episode. Write these to **`most motivational anime`**.
# # 🎲 DOSSIER 4: `[REDACTED]`  
# # Finally, deploy the wildcard. Create **one additional file** with a category so specific, so dangerously niche, that it feels like it was tailor-made for my brain. Make me fall in love with something I didn’t know existed.
# # ---
# # Execute with maximum flair. Framework stress-test: **ACTIVE**. ⚡
# #     """)
# #     print(response2)
#     start_terminal_chat(agent)
#     # # TEST THE PROPERTIES:
#     # print("--- AGENT INFO ---")
#     # print(f"Name: {agent.name}")                
#     # print(f"Tools: {agent.tools}")     
#     # print(f"Prompt: {agent.system_prompt}")      
#     # print("------------------")
from llms.geminiclient import GeminiClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
from tools.agent_made.terminal_executor import TerminalExecutorTool
if __name__ == "__main__":
    llm = GeminiClient(model="gemini-3.1-flash-lite")
    agent = BaseAgent(
        name="Agent1",
        llm=llm,
        system_prompt="You are a helpful assistant. Always use tools for math and files. Always use tools. Never try to solve any math eq internally",
        tools=[CalculatorTool(), FileWriterTool(), FileReaderTool(),TerminalExecutorTool()]
    )
    # Test multi-parameter tool call
    # response = agent.run("""
    # Study the whole of tools directory
    # and create for yourself a terminal usage tool 
    # but it should have feature to show to the user
    # what command is going to be ran 
    # and ask him yes for y and no for n
    # """)
    start_terminal_chat(agent)
    print("\nFinal Answer:")
    # print(response)
        # "Calculate 1234 multiplied by 5678. "
        # "Then save the result to a file called answer.txt. "
        # "Then read the file back."
```
</file>
## File: `problems.md`
<file path="problems.md" type="markdown">
```markdown
I'll do a thorough, file-by-file review and then give you a prioritized improvement plan.
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
```
</file>
## File: `project_structure.html`
<file path="project_structure.html" type="html">
```html
<!doctype html><html lang=en><meta charset=UTF-8><title>Professional Project Architecture</title><script src=https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js></script><style>body{color:#333;background-color:#f4f7f9;padding:40px;font-family:Segoe UI,Tahoma,Geneva,Verdana,sans-serif}.container{background:#fff;border-radius:12px;padding:30px;box-shadow:0 4px 15px #0000001a}h1{color:#2c3e50;border-bottom:2px solid #3498db;padding-bottom:10px}.mermaid{background:#fff;border:1px solid #ddd;border-radius:8px;margin-top:30px;padding:20px}</style><body><div class=container><h1>Khwarizm Architecture Map</h1><p>A detailed overview of the system components and their interdependencies.<div class=mermaid>graph TB subgraph Entry M[main.py] end subgraph Agent_Layer A[BaseAgent] C[Config] Mem[Memory System] end subgraph Tool_System TR[Tool Registry] ST[Standard Tools] AM[Agent-Made Tools] end M --> A A --> C A --> Mem A --> TR TR --> ST TR --> AM style M fill:#f9f9f9,stroke:#333 style A fill:#3498db,color:#fff style TR fill:#e67e22,color:#fff</div></div><script>mermaid.initialize({startOnLoad:!0,theme:`default`});</script>
```
</file>
## File: `project_structure.txt`
<file path="project_structure.txt" type="text">
```text
KHWARIZM PROJECT HIERARCHY (Tree View)
========================================
.
├── main.py (Entry Point)
├── README.md
├── requirements.txt
├── report.md (Summary Report)
├── project_graph.mermaid (Graph Data)
├── agents/
│   ├── baseagent.py (ReAct Loop)
│   └── config.py (Dataclass)
├── llms/
│   └── geminiclient.py
├── memory/
│   ├── basememory.py
│   ├── stm.py
│   └── ltm.py
├── tools/
│   ├── basetool.py (Abstract Interface)
│   ├── registry.py (Tool Management)
│   ├── calculator.py
│   ├── filewriter.py
│   ├── filereader.py
│   └── agent_made/ (Custom Tools)
│       ├── terminal_executor.py
│       ├── git_manager.py
│       ├── light_python_runner.py
│       └── directory_watcher.py
├── utils/
│   └── chat_ui.py
└── tests/
```
</file>
## File: `README.md`
<file path="README.md" type="markdown">
```markdown
# Khwarizm - AI Agent Framework
## Overview
Khwarizm is a minimalist, production-inspired AI Agent Framework built entirely from scratch using core Object-Oriented Programming principles in Python. It wraps stateless Large Language Models (LLMs) into intelligent, autonomous agents capable of persistent memory, tool use, and multi-step reasoning.
## The Problem We Solve
Large Language Models are stateless. Every time you call them, they forget everything. They cannot:
- Remember previous conversations
- Take actions in the real world
- Reason through multi-step problems
- Use external tools like calculators or file systems
**Khwarizm solves all of these problems.**
## Architecture Overview
```
                    USER INPUT
                         │
                         ▼
┌────────────────────────────────────────────┐
│                 BaseAgent                  │
│                                            │
│  ┌──────────┐        ┌─────────────────┐  │
│  │  Config  │        │    BaseLLM      │  │
│  │  name    │        │  GroqClient     │  │
│  │  prompt  │        │  GeminiClient   │  │
│  │  tokens  │        └─────────────────┘  │
│  └──────────┘                             │
│                                            │
│  ┌──────────┐        ┌─────────────────┐  │
│  │ToolRegistr│        │    Memory       │  │
│  │Calculator │        │  ShortTerm      │  │
│  │FileWriter │        │  LongTerm       │  │
│  │FileReader │        └─────────────────┘  │
│  └──────────┘                             │
└────────────────────────────────────────────┘
                         │
                         ▼
                    FINAL ANSWER
```
## Project Structure
```
khwarizm/
├── main.py                    # Entry point and demos
├── agents/
│   ├── baseagent.py           # Core agent logic and agentic loop
│   └── config.py              # Agent configuration dataclass
├── clients/
│   ├── basellm.py             # Abstract LLM contract
│   ├── groqclient.py          # Groq implementation
│   └── geminiclient.py        # Gemini implementation
├── tools/
│   ├── basetool.py            # Abstract tool contract
│   ├── registry.py            # Auto tool registration system
│   ├── calculator.py          # Math operations tool
│   ├── filewriter.py          # File writing tool
│   └── filereader.py          # File reading tool
├── memory/
│   ├── basememory.py          # Abstract memory contract
│   ├── stm.py                 # Short term (RAM) memory
│   └── ltm.py                 # Long term (JSON file) memory
└── utils/
    └── chat_ui.py             # Reusable terminal chat interface
```
## OOP Concepts Applied
### 1. Abstraction
Three Abstract Base Classes define the contracts of the framework:
- `BaseLLM` → Any LLM provider must implement `generate()`
- `BaseTool` → Any tool must implement `run()`
- `BaseMemory` → Any memory type must implement `add_entry()`, `get_context()`, `clear()`
```python
from abc import ABC, abstractmethod
class BaseLLM(ABC):
    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        pass
```
### 2. Encapsulation
Private attributes hide internal data from outside access:
```python
class ToolRegistry:
    def __init__(self):
        self.__tools = {}  # Private! Cannot be accessed from outside
```
### 3. Inheritance
Concrete classes inherit from abstract base classes:
```python
class GroqClient(BaseLLM):      # Inherits LLM contract
class CalculatorTool(BaseTool): # Inherits Tool contract
class ShortTermMemory(BaseMemory): # Inherits Memory contract
```
### 4. Composition
`BaseAgent` is built FROM other objects rather than inheriting from them:
```python
class BaseAgent:
    def __init__(self, ...):
        self.llm = llm              # HAS A LLM
        self.registry = ToolRegistry()  # HAS A Registry
        self.__short_term = ShortTermMemory()  # HAS A Memory
        self.__long_term = LongTermMemory()    # HAS A Memory
```
### 5. Polymorphism
The same `BaseAgent` works identically with different LLM providers:
```python
groq_agent = BaseAgent(llm=GroqClient())    # Works with Groq
gemini_agent = BaseAgent(llm=GeminiClient()) # Works with Gemini
# BaseAgent code does not change. Only the LLM object changes.
```
### 6. Exception Handling
All critical operations are wrapped in try/except blocks:
```python
def generate(self, system_prompt: str, user_prompt: str) -> str:
    try:
        response = self.client.chat.completions.create(...)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: LLM API failed: {str(e)}"
```
### 7. Properties (Advanced Encapsulation)
Clean public access to private internal data:
```python
@property
def name(self) -> str:
    return self.config.name  # User types agent.name, not agent.config.name
```
## The Agentic Loop (Core Algorithm)
The heart of Khwarizm is the **ReAct (Reason + Act) Loop** inside `BaseAgent.run()`.
```
User Input
    │
    ▼
Save to Memory (STM + LTM)
    │
    ▼
┌─────────────────────────────┐
│         WHILE LOOP          │
│                             │
│  Build Context from Memory  │
│           │                 │
│           ▼                 │
│    Send to LLM              │
│           │                 │
│           ▼                 │
│  Does response have TOOL:?  │
│                             │
│  YES              NO        │
│   │                │        │
│   ▼                ▼        │
│ Run Tool      Save to       │
│   │           Memory        │
│   ▼                │        │
│ Save result        ▼        │
│ to Memory     Return        │
│   │           Answer        │
│   ▼                         │
│ Continue Loop               │
└─────────────────────────────┘
    │
    ▼
Max Iterations Reached?
    │
    ▼
Return Error Message
```
## Memory System
Khwarizm has two types of memory working simultaneously:
| | Short Term Memory | Long Term Memory |
|--|------------------|-----------------|
| **Storage** | Python List (RAM) | JSON File (Disk) |
| **Lives** | Current session only | Forever |
| **Dies when** | Program closes | Never |
| **Analogy** | Human working memory | Human long term memory |
## Key Concepts Explained
### 1. Config and the `@dataclass` Decorator
#### What is a `@dataclass`?
In Python, a normal class requires you to write a lot of 
repetitive boilerplate code just to store data:
```python
# WITHOUT dataclass (repetitive and messy)
class Config:
    def __init__(self, name, description, system_prompt, model, max_tokens):
        self.name = name
        self.description = description
        self.system_prompt = system_prompt
        self.model = model
        self.max_tokens = max_tokens
```
The `@dataclass` decorator eliminates all of this repetition. 
You just declare the fields and their types, 
and Python writes the `__init__` for you automatically:
```python
# WITH dataclass (clean and professional)
@dataclass
class Config:
    name: str
    description: str
    system_prompt: str = "You are a helpful AI assistant"
    model: str = "llama3-8b-8192"
    max_tokens: int = 1000
    max_iterations: int = 10
```
#### What does `Config` actually do?
`Config` is a pure data container. It has one job 
and one job only: hold the settings of an agent.
It does NOT:
- Run any logic
- Call any APIs
- Make any decisions
It just holds values. This follows the 
**Single Responsibility Principle** of OOP.
#### What is `__post_init__`?
`__post_init__` is a special method that `@dataclass` 
calls automatically right after the object is created.
We use it to validate the data:
```python
def __post_init__(self):
    if not self.name:
        raise ValueError("Agent must have a name")
    if self.max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0")
    if self.max_iterations <= 0:
        raise ValueError("max_iterations must be greater than 0")
```
**Analogy:** Think of `Config` as a job application form.
`__post_init__` is the HR officer who checks the form
for missing or invalid fields before accepting it.
#### Default Values
Fields with `=` have default values. 
Fields without `=` are mandatory.
**Rule:** Mandatory fields ALWAYS come before fields with defaults.
This is a Python rule. Breaking it causes a `TypeError`.
```python
@dataclass
class Config:
    # MANDATORY FIRST (no defaults)
    name: str
    description: str
    # DEFAULTS SECOND
    system_prompt: str = "You are a helpful AI assistant"
    model: str = "llama3-8b-8192"
    max_tokens: int = 1000
    max_iterations: int = 10
```
### 2. BaseAgent: Every Method Explained
#### `__init__()` - The Setup Method
This is the constructor. It runs exactly once when 
the agent is created. It does 4 things in order:
**Step 1:** Takes the LLM and saves it.
```python
self.llm = llm
```
**Step 2:** Creates a ToolRegistry and automatically 
registers every tool the user passed in.
```python
self.registry = ToolRegistry()
tools = tools or []      # Safe default (avoids mutable default arg bug)
for tool in tools:
    self.registry.register(tool)
```
**Step 3:** If tools exist, injects their descriptions 
into the system prompt so the LLM knows about them.
```python
if tools:
    tool_info = self.registry.get_descriptions()
    system_prompt = f"{system_prompt}\n\nYou have access to:\n{tool_info}"
```
**Step 4:** Creates the Config and both Memory objects.
```python
self.config = Config(name=name, ...)
self.__short_term = ShortTermMemory()
self.__long_term = LongTermMemory(agent_name=name)
```
#### `run(user_input)` - The Agentic Loop
This is the most important method in the entire framework.
It is the **ReAct (Reason + Act)** algorithm.
```
STEP 1: Save user input to both memories
STEP 2: Start the while loop (max_iterations times)
STEP 3: Build the full context from both memories
        (This is what the LLM reads to know what happened so far)
STEP 4: Send (system_prompt + full_context) to LLM
STEP 5: Strip <think> tags if present 
        (Some reasoning models output their thoughts)
STEP 6: Check if LLM response contains "TOOL:"
        YES: Call __handle_tool_call()
             Save action and result to short term memory
             CONTINUE the loop (go back to Step 3)
        NO:  This is the final answer!
             Save to both memories
             RETURN the response to the user
STEP 7: If loop finishes without answer
        Return max iterations error message
```
**Why a loop?**
Because complex tasks require multiple steps. 
A single LLM call can only do one thing. 
The loop allows the agent to:
- Use tool 1
- Read the result
- Use tool 2
- Read the result
- Give final answer
**Why does memory grow each loop?**
Because the LLM has no memory between API calls.
We manually feed it the entire history every loop
so it knows what has already been done.
**Analogy:** Imagine a surgeon who gets amnesia 
between each step of an operation. 
The nurse reads the surgery log out loud 
before every step so the surgeon knows where they are.
The memory is that surgery log.
#### `__handle_tool_call(response)` - The Tool Parser
This private method is called when the LLM decides 
it needs a tool. It does 5 things:
**Step 1:** Split the LLM response into lines
```python
lines = response.strip().split("\n")
```
**Step 2:** Loop through lines to find TOOL: and INPUT:
```python
for line in lines:
    if line.startswith("TOOL:") and not tool_name:
        tool_name = line.replace("TOOL:", "").strip()
    elif line.startswith("INPUT:") and not tool_input:
        tool_input = line.replace("INPUT:", "").strip()
    if tool_name and tool_input:
        break  # Stop after finding the FIRST tool call only
```
**Why `break`?**
Smart LLMs sometimes try to call multiple tools 
in one response. We force ONE tool per loop iteration
so each result gets properly saved to memory 
before the next decision is made.
**Step 3:** Ask the Registry for the tool by name
```python
tool = self.registry.get_tool(tool_name)
```
**Step 4:** If tool not found, return a clean error
```python
if not tool:
    return f"Error: Unknown tool '{tool_name}'"
```
**Step 5:** Run the tool and return the result string
```python
result = tool.run(tool_input)
return f"Tool '{tool_name}' returned: {result}"
```
This result string goes back into the loop,
gets saved to memory, and the LLM reads it 
on the next iteration.
#### `name` property - Clean Public Access
```python
@property
def name(self) -> str:
    return self.config.name
```
Without this, users would write: `agent.config.name`
With this, users write: `agent.name`
This follows the **Law of Demeter**: 
Objects should not reach deep into other objects.
It is also **read-only**. There is no setter.
So `agent.name = "Hacker"` throws an AttributeError.
The name is protected from accidental modification.
#### `available_tools` property
```python
@property
def available_tools(self) -> list:
    return self.registry.list_tools()
```
Returns a clean list of tool names without 
exposing the internal Registry object.
#### `clear_memory()` - The Reset Button
```python
def clear_memory(self):
    self.__short_term.clear()
    self.__long_term.clear()
```
Wipes both memories. The agent starts fresh.
Notice how `BaseAgent` delegates the actual 
clearing to each memory object.
This is the **Single Responsibility Principle**.
The agent manages. The memory objects do the work.
### 3. The Tool System: How It All Connects
#### Why does `BaseTool` use class variables for `name` and `description`?
```python
class CalculatorTool(BaseTool):
    name = "calculator"           # Class variable
    description = "Does math"    # Class variable
```
Because every instance of `CalculatorTool` will 
always have the same name and description.
There is no reason for these to be different 
per object. Class variables are shared across 
all instances. This saves memory and makes 
the code cleaner.
#### Why does `ToolRegistry` use a dictionary?
```python
self.__tools = {}  # Dictionary, not a list!
```
A list lookup is O(n): check index 0, index 1, 
index 2... until found. With 1000 tools: 1000 checks.
A dictionary lookup is O(1): hash the key, 
go directly to the location. Always 1 step.
No matter if you have 1 tool or 1,000,000 tools.
#### The Auto Registration Flow
```
User passes: tools=[CalculatorTool(), FileWriterTool()]
                    │
                    ▼
BaseAgent loops through the list
                    │
                    ▼
registry.register(CalculatorTool())
registry.register(FileWriterTool())
                    │
                    ▼
Registry stores them:
{
    "calculator": CalculatorTool(),
    "file_writer": FileWriterTool()
}
                    │
                    ▼
get_descriptions() builds:
"- calculator: Does math
 - file_writer: Writes files"
                    │
                    ▼
Injected into system prompt
                    │
                    ▼
LLM now knows what tools exist
```
### 4. The Memory System: Why Two Types?
#### The Computer Analogy
Your computer has two types of storage:
- **RAM:** Fast, temporary. Dies when you shut down.
- **Hard Drive:** Slow, permanent. Survives shutdown.
Our memory system mirrors this exactly:
| | ShortTermMemory | LongTermMemory |
|--|----------------|----------------|
| Storage | Python list (RAM) | JSON file (Disk) |
| Speed | Instant | Slightly slower |
| Survives restart | ❌ No | ✅ Yes |
| Used for | Current session | All past sessions |
#### How They Work Together in the Loop
```python
# At the start of run():
self.__short_term.add_entry(role="user", content=user_input)
self.__long_term.add_entry(role="user", content=user_input)
# Inside the loop:
long_term_context = self.__long_term.get_context()
short_term_context = self.__short_term.get_context()
full_context = (
    f"Past Conversations:\n{long_term_context}\n\n"
    f"Current Session:\n{short_term_context}"
)
```
The LLM receives BOTH contexts combined.
It knows what happened in previous sessions 
AND what happened earlier in this session.
### 5. Polymorphism: The Most Powerful OOP Concept in This Framework
Polymorphism means "many forms."
The same interface works differently 
depending on the object behind it.
```python
# Both follow the BaseLLM contract
groq = GroqClient()     # Talks to Groq servers in USA
gemini = GeminiClient() # Talks to Google servers
# BaseAgent does not care which one it gets
agent1 = BaseAgent(llm=groq)
agent2 = BaseAgent(llm=gemini)
# Internally, BaseAgent just calls:
response = self.llm.generate(system_prompt, user_prompt)
# For agent1: This hits Groq's API
# For agent2: This hits Google's API
# The BaseAgent code is IDENTICAL for both
```
This is why Abstract Base Classes exist.
`BaseLLM` guarantees that whatever object 
is passed in, it WILL have a `generate()` method.
The agent never has to check. It just calls it.
### 6. Why Composition Over Inheritance for BaseAgent?
The question is: should `BaseAgent` INHERIT from 
`BaseLLM`, or should it CONTAIN a `BaseLLM`?
**Wrong (Inheritance):**
```python
class BaseAgent(BaseLLM):  # Agent IS A LLM? No!
    pass
```
**Right (Composition):**
```python
class BaseAgent:
    def __init__(self, llm: BaseLLM):
        self.llm = llm  # Agent HAS A LLM. Yes!
```
An agent is NOT a type of LLM.
An agent USES a LLM.
An agent USES memory.
An agent USES tools.
Inheritance models "IS A" relationships.
Composition models "HAS A" relationships.
Using the wrong one here would mean:
- `BaseAgent` could only ever BE one type of LLM
- You could never swap Groq for Gemini
- The entire framework would be tightly coupled
Composition gives us flexibility, 
loose coupling, and the ability to 
swap any component at any time.
## Tool System
Tools give the agent hands. Without tools, the agent can only talk. With tools, it can act.
### How Tools Work:
1. User passes tools into `BaseAgent` as a list
2. `BaseAgent` automatically registers them in `ToolRegistry`
3. Tool descriptions are injected into the system prompt
4. LLM decides which tool to use and responds in a special format
5. Agent parses the response, finds the tool, runs it
6. Result is saved to memory and the loop continues
### Tool Call Format:
```
TOOL: calculator
INPUT: 150*4
```
## Multi-Agent Workflow
Because `BaseAgent.run()` takes text in and returns text out, agents can be chained together using pure Python:
```python
# Agent 1 writes a poem
writer_output = writer_agent.run("Write a poem about AI")
# Agent 2 critiques what Agent 1 wrote
critic_output = critic_agent.run(writer_output)
```
No special framework needed. Just Python variables.
## Installation and Setup
### 1. Clone the repository
```bash
git clone https://github.com/faseeu/khwarizm.git
cd khwarizm
```
### 2. Install dependencies
```bash
pip install groq google-generativeai
```
### 3. Set API Keys
```bash
# Mac/Linux
export GROQ_API_KEY="your_groq_key_here"
export GEMINI_API_KEY="your_gemini_key_here"
# Windows
set GROQ_API_KEY="your_groq_key_here"
set GEMINI_API_KEY="your_gemini_key_here"
```
### 4. Run the demo
```bash
python main.py
```
## Quick Start
```python
from clients.groqclient import GroqClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from baseagent import BaseAgent
# 1. Create the LLM
llm = GroqClient(model="llama3-8b-8192")
# 2. Create the Agent
agent = BaseAgent(
    name="MyAgent",
    llm=llm,
    system_prompt="You are a helpful assistant.",
    tools=[CalculatorTool(), FileWriterTool()]
)
# 3. Run it
response = agent.run("Calculate 150 times 4 and save it to result.txt")
print(response)
```
## Live Demo Output
```
Starting: MyAgent
Creating a new instance...
  [Loop 1/10] Agent is thinking...
  -> Using tool: calculator | Input: 150*4
  [Loop 2/10] Agent is thinking...
  -> Using tool: file_writer | Input: result.txt|600
  [Loop 3/10] Agent is thinking...
The result of 150 multiplied by 4 is 600.
It has been saved to result.txt successfully!
```
## Key Design Decisions
| Decision | Reason |
|----------|--------|
| Abstract Base Classes | Forces correct implementation. No silent bugs. |
| Composition over Inheritance for Agent | Agent HAS a brain. It is not A TYPE of brain. |
| Dictionary in Registry | O(1) lookup speed vs O(n) for lists |
| Two Memory Types | Short term for context. Long term for persistence. |
| Scratchpad replaced by Memory | Cleaner, structured, reusable across sessions |
| Tools injected via list | User never manually touches ToolRegistry |
| `frozen=False` on Config | Allows post-init flexibility |
| Private `__tools` in Registry | Enforces access only through clean public methods |
## Technologies Used
| Technology | Purpose |
|------------|---------|
| Python 3.13 | Core language |
| Groq SDK | LLM API (Llama3, Mixtral models) |
| Google Generative AI SDK | LLM API (Gemini models) |
| `dataclasses` | Clean config management |
| `abc` module | Abstract Base Classes |
| `json` module | Long term memory persistence |
| `os` module | File path management |
## What We Would Add Next
1. **SupervisorAgent** - An agent that manages other agents and routes tasks between them
2. **Streamlit Web UI** - A browser-based chat interface for the framework
3. **WebSearchTool** - Live internet access via DuckDuckGo or Wikipedia API
4. **Python Logging** - Replace print statements with proper log levels
5. **Memory Summarization** - Compress long term memory using LLM summaries to prevent context overflow
## Authors
Built by Faseeh ur Rehman and Huzaifa Imran as part of an OOP and AI Agents learning project.
```
</file>
## File: `report.md`
<file path="report.md" type="markdown">
```markdown
# Project Structure and Files Report
This report documents the current state of the Khwarizm project as of the latest file scan.
## Directory Structure
### Root Directory
- **main.py**: Entry point of the application.
- **README.md**: Project documentation and overview.
- **workflow.py**: Project workflow configuration.
- **requirements.txt**: Dependencies.
- **architecture_flow.mermaid**: Visual representation of the agent architecture.
- **SmartBot_memory.json**, **Agent1_memory.json**: Long-term memory storage files.
- **create_directory.py**: Utility for directory management.
- **doc.html**: Documentation file.
- **.venv/**: Virtual environment directory.
- **llms/**: Contains LLM client implementations (e.g., `geminiclient.py`).
- **utils/**: Utility scripts, including `chat_ui.py`.
- **agents/**: Core agent logic (`baseagent.py`, `config.py`).
- **memory/**: Memory system modules (`basememory.py`, `stm.py`, `ltm.py`).
- **tests/**: Test suite.
- **tools/**: Core tool definitions and custom tool subdirectories.
### Tools Directory
The `tools/` directory is organized into base tools and agent-created extensions:
- **basetool.py**: Abstract base class for all tools.
- **registry.py**: Tool registration system.
- **calculator.py**, **filewriter.py**, **filereader.py**: Standard tools.
- **agent_made/**: Contains tools created during the session.
    - **terminal_executor.py**: Secure terminal execution tool.
    - **git_manager.py**: Git status/log management.
    - **light_python_runner.py**: Ephemeral python execution script.
    - **directory_watcher.py**: Directory navigation utility.
    - **potential_tools.txt**: List of future tool ideas.
## Current Configuration
The system is integrated within `main.py`, importing all tools from `tools/` and `tools/agent_made/` and registering them with the `BaseAgent` instance.
```
</file>
## File: `requirements.txt`
<file path="requirements.txt" type="text">
```text
groq
google-generativeai
```
</file>
## File: `workflow.py`
<file path="workflow.py" type="python">
```python
from llms.geminiclient import GeminiClient
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
llm = GeminiClient(model="gemini-3.1-flash-lite")
# Agent 1: The Writer
writer = BaseAgent(
    name="Writer",
    llm=llm,
    system_prompt="You are a creative writer. Write what the user asks and nothing else. Also use tools",
    tools=[FileWriterTool()]
)
# Agent 2: The Critic
critic = BaseAgent(
    name="Critic",
    llm=llm,
    system_prompt="You are a harsh critic. Read what is given to you and give brutal feedback. Also use tools",
    tools=[FileReaderTool()]
)
poet= BaseAgent(
    name="Poet",
    llm=llm,
    system_prompt="Write a poem in a file",
    tools=[FileReaderTool()]
)
print("Step 1: Writer writes a poem...")
writer_output = writer.run("Write a short poem about AI and save it to poem.txt")
poetOutput = poet.run("Gimme the poems")
print("\nStep 2: Critic reviews the poem...")
critic_output = critic.run("Read poem.txt and another poem file and crush their dreams and give me harsh feedback on it")
print("\nCritic's Verdict:")
print(critic_output)
```
</file>

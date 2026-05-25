# Project Context Analysis

```
KHWARIZM PROJECT HIERARCHY (Tree View)
========================================
├── main.py (Entry Point)
├── README.md
├── requirements.txt
├── project_graph.mermaid (Graph Data)
├── agents/
│   ├── baseagent.py (ReAct Loop)
│   └── config.py (Dataclass)
├── llms/
│   └── basetool.py
│   └── groqclient.py
│   └── geminiclient.py
├── memory/
│   ├── memory.py
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


## File: filewriter.py
```
from tools.basetool import BaseTool

class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file on the local filesystem."
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

            with open(filename, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"

```


## File: filereader.py
```
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


## File: calculator.py
```
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


## File: registry.py
```
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


## File: basetool.py
```
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


## File: geminiclient.py
```
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


## File: groqclient.py
```
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


## File: basellm.py
```
from abc import ABC , abstractmethod

class BaseLLM(ABC):
    
    @abstractmethod
    def generate(self, system_prompt, user_prompt) ->str:
        raise NotImplementedError
```


## File: utils/chat_ui.py
```
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


## File: stm.py
```
from memory.memory import BaseMemory


class ShortTermMemory(BaseMemory):

    def __init__(self):
        self.__history = []
    
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })

     
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


## File: ltm.py
```
import json
import os
from memory.memory import BaseMemory

class LongTermMemory(BaseMemory):
    
    def __init__(self, agent_name: str):
        self.__file_path = f"{agent_name}_memory.json"
        self.__history = self.__load_from_file()
    
    def add_entry(self, role: str, content: str):
        self.__history.append({
            "role": role,
            "content": content
        })
        self.__save_to_file()
    
    def get_context(self) -> str:
        if not self.__history:
            return ""
        
        context = ""
        for entry in self.__history:
            context += f"{entry['role']}: {entry['content']}\n"
        return context
    
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


## File: memory.py
```
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

## File: config.py
```
from dataclasses import dataclass

@dataclass
class Config:
#---Identity
    name: str
    # model: str
    description: str = "This AI agent is like an AI from the future and will give you futuristic explainations for every question you ask."

#---Prompts
    system_prompt: str = "You are a helpful AI assistant."
    user_prompt: str=""

#---LLM Settings
    
    max_tokens: int = 1000

#---Behavior settings
    max_iterations: int = 50

    def __post_init__(self):
        if not self.name:
            raise ValueError("Agent must have a name") 
        if self.max_tokens <= 0:
            raise ValueError("max_tokens must be greater than 0")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be greater than 0")
```  



## File: main.py
This is the primary entry point for the application.
```
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
### Code Breakdown
- **Imports**: Loads the `GeminiClient` (LLM interface), core `BaseAgent` logic, and various standard/custom tools from the `tools` and `tools/agent_made` directories. It also imports `start_terminal_chat` from `utils` to handle the interaction loop.
- **Initialization**: 
    - Instantiates the `GeminiClient` using the "gemini-3.1-flash-lite" model.
    - Configures the `BaseAgent` with a specific system prompt that mandates tool usage for calculations and file operations.
    - Registers a list of tools including `CalculatorTool`, `FileWriterTool`, `FileReaderTool`, and the custom tools (`TerminalExecutorTool`, `GitManagerTool`, `LightPythonRunnerTool`, `DirectoryWatcherTool`).
- **Execution**: Calls `start_terminal_chat(agent)` to begin the interactive session.

### Flow and Connections
- `main.py` acts as the orchestrator. It ties the LLM, the Agent logic, and the Tool library together. When the user inputs a prompt, `start_terminal_chat` passes it to the `BaseAgent`, which uses the `GeminiClient` to process the request and decide whether to invoke a tool from the registered list.

## File: tools/calculator.py
This is a standard utility tool for performing arithmetic.

### Code Breakdown
- **Inheritance**: Inherits from `BaseTool`.
- **Definition**: Defines the tool name as "calculator" and provides a description and parameter schema for the LLM.
- **run() method**: 
    - Extracts the "expression" parameter from the input dictionary.
    - Performs sanitization (removing trailing "=" characters).
    - Uses Python's `eval()` function to compute the result.
    - Returns the result as a string or captures exceptions if the input is invalid.

### Flow and Connections
- This tool is registered in the `tools` list in `main.py`. When the `BaseAgent` determines a math operation is needed, it triggers this class's `run()` method, effectively delegating computation outside of the LLM context to ensure accuracy.

## File: tools/filewriter.py
This is a standard utility tool for writing data to the local disk.

### Code Breakdown
- **Inheritance**: Inherits from `BaseTool`.
- **Definition**: Defines the tool name as "file_writer" and specifies the "filename" and "content" parameters.
- **run() method**: 
    - Retrieves filename and content from parameters.
    - Validates the filename presence.
    - Uses the standard Python `open(filename, 'w')` context manager to write content.
    - Returns a success message or an error string if an exception occurs.

### Flow and Connections
- This tool provides the persistence layer for the agent. It is called by the `BaseAgent` whenever the agent needs to save notes, logs, or results, allowing the agent to manage its own knowledge base beyond the volatile session memory.

## File: tools/filereader.py
This is a standard utility tool for reading data from the local disk.

### Code Breakdown
- **Inheritance**: Inherits from `BaseTool`.
- **Definition**: Defines the tool name as "file_reader" and specifies the "filename" parameter.
- **run() method**: 
    - Retrieves the filename from parameters.
    - Uses the standard Python `open(filename, 'r')` context manager to read content.
    - Implements basic error handling for `FileNotFoundError` and general exceptions.
    - Returns the file content prepended with a descriptor or an error message.

### Flow and Connections
- This tool is the counterpart to `FileWriterTool`. It enables the agent to inspect the current state of its project workspace, allowing it to "study" files as requested by the user and maintain contextual awareness.

## File: tools/agent_made/terminal_executor.py
This is a custom tool designed to provide safe shell interaction.

### Code Breakdown
- **Inheritance**: Inherits from `BaseTool`.
- **Logic**: 
    - Uses the `subprocess` module to execute commands.
    - **Safety Layer**: Implements a `print` statement followed by `input()` to force human-in-the-loop verification before execution. 
    - **Execution**: If the user provides 'y', it runs the command using `subprocess.check_output`, capturing the output and error streams.
- **Flow and Connections**: This tool is part of the `agent_made` package. It provides the agent with the ability to interact with the OS while ensuring the user retains control over sensitive or potentially harmful operations.

## File: tools/agent_made/git_manager.py
A specialized tool for tracking project history using git.

### Code Breakdown
- **Inheritance**: Inherits from `BaseTool`.
- **Logic**: 
    - Concatenates "git" with a user-provided command.
    - **Verification**: Like the `TerminalExecutorTool`, it requires explicit user confirmation via `input()`.
    - **Execution**: Runs the constructed command via `subprocess` and returns the command output or captures errors.
- **Flow and Connections**: Extends the `agent_made` suite to allow the agent to monitor project health, check logs, and inspect changes, facilitating autonomous development cycles.

## File: tools/agent_made/light_python_runner.py
A tool for ephemeral Python script execution.

### Code Breakdown
- **Inheritance**: Inherits from `BaseTool`.
- **Logic**: 
    - Defines a temporary directory `.ephemeral_venv`.
    - **Cleanup**: Checks for and deletes any existing `.ephemeral_venv` directory before starting.
    - **Execution**: Constructs a shell command that creates a virtual environment, runs the specified Python script, and uses a `finally` block to delete the environment immediately afterward.
    - **Verification**: Requires user confirmation before execution.
- **Flow and Connections**: Part of the `agent_made` toolkit. It allows the agent to safely execute user-provided or generated code without affecting the host environment, satisfying the "run-once-and-die" requirement.

## File: tools/agent_made/directory_watcher.py
A simple utility for inspecting the project directory structure.

### Code Breakdown
- **Inheritance**: Inherits from `BaseTool`.
- **Logic**: 
    - Uses `os.listdir()` to scan the specified path.
    - Returns a comma-separated list of filenames.
- **Flow and Connections**: This tool allows the agent to navigate the project workspace programmatically, acting as the "eyes" of the agent to identify available files and inform subsequent read/execute operations.

## File: workflow.py
A demonstration script for multi-agent interaction.

### Code Breakdown
- **Initialization**: Defines multiple `BaseAgent` instances ("Writer", "Critic", "Poet") with varying system prompts and specific tools assigned to each.
- **Workflow Execution**: 
    - The "Writer" agent performs a file writing task.
    - The "Poet" agent attempts retrieval of generated content.
    - The "Critic" agent processes both the writer's and poet's work to provide feedback.
- **Flow and Connections**: This file acts as a testing suite to demonstrate the agent architecture. It highlights how different system prompts and tool access levels can lead to specialized agent behavior within a single shared context.

## File: requirements.txt
Defines project dependencies.

### Code Breakdown
- **Content**: Lists `groq` and `google-generativeai` as the required external libraries.
- **Flow and Connections**: These packages are vital for the agent's LLM connectivity. `google-generativeai` is used by the `GeminiClient` to interface with Google's models, while `groq` provides an alternative inference provider if needed.

## File: main2.py
A legacy/development sandbox file.

### Code Breakdown
- **Purpose**: This file contains commented-out code representing previous iterations of the agent's setup and testing. It demonstrates alternative configurations (using different LLMs like `GroqClient` vs `GeminiClient`) and discarded test scenarios.
- **Flow and Connections**: While currently non-functional due to being commented out, it serves as a historical record of hte project's evolution, showing the transition from a multi-LLM experimental phase to the current, more stable `main.py` implementation.

## File: utils/chat_ui.py
The core communication interface for the user.

### Code Breakdown
- **Function**: `start_terminal_chat(agent)`
    - Initializes a loop that prompts the user for input.
    - Hands the input to the `agent.run(user_input)` method.
    - Prints the agent's response to the terminal.
    - Handles "exit" or "quit" commands to break the loop.
- **Flow and Connections**: This is the glue between the human and the agent. It continuously calls `BaseAgent.run()`, which triggers the LLM logic, allowing for sustained, conversational interaction with the tool-enabled system.

## File: llms/geminiclient.py
The Gemini LLM interface client.

### Code Breakdown
- **Initialization**: Retrieves `GEMINI_API_KEY` from the environment, configures the `google.generativeai` SDK, and initializes a `GenerativeModel`.
- **generate() method**: Constructs a full prompt by combining system instructions and user input, then calls the model via the API.
- **Flow and Connections**: This acts as the "brain" interface. It is consumed by the `BaseAgent` to fetch intelligence for decision-making and text generation, isolating the complexities of API communication from the core agent logic.

## File: agents/baseagent.py
The core engine of the agentic framework.

### Code Breakdown
- **Initialization**:
    - Sets up the LLM, a `ToolRegistry`, and `ShortTermMemory`/`LongTermMemory` instances.
    - Dynamically builds the `system_prompt` by appending tool definitions and strict operating rules.
- **Execution (`run()` method)**:
    - Maintains a loop (`iterations`) that builds context from memory, calls the LLM, handles tool usage via `__handle_tool_call()`, and updates memories.
- **Tool Handling**: `__handle_tool_call()` uses `xml.etree.ElementTree` to parse the LLM's structured tool output, validate it against the registry, and execute it, returning the result to the conversation stream.
- **Flow and Connections**: This is the central controller. It bridges user input, tool logic, and LLM reasoning. It ensures that every action is stateful (via memory) and follows the constraints defined in the system prompt.

## File: memory/stm.py
The short-term memory management module.

### Code Breakdown
- **Inheritance**: Inherits from `BaseMemory`.
- **Logic**:
    - Uses a private list `__history` to store dictionaries of role/content pairs.
    - `add_entry()` appends interactions (user input and assistant/tool output) to the list.
    - `get_context()` iterates through the list to generate a readable string of recent interactions for the LLM.
- **Flow and Connections**: This file manages volatile, session-specific context. It ensures the agent maintains focus during a long-running conversation, providing the LLM with the most immediate preceding turns in the current `start_terminal_chat` loop.

## File: memory/ltm.py
The long-term memory management module.

### Code Breakdown
- **Inheritance**: Inherits from `BaseMemory`.
- **Logic**:
    - Uses a JSON file (`{agent_name}_memory.json`) for persistence.
    - `add_entry()` appends data and triggers an automatic `__save_to_file()` call.
    - Includes robust error handling for file I/O, allowing the agent to start fresh if the JSON file is corrupted.
- **Flow and Connections**: This module enables persistent state. By saving interactions to the local filesystem, it allows the agent to "remember" previous tasks across different sessions, provided it uses the same agent name.

## File: agents/config.py
The configuration schema for the agent.

### Code Breakdown
- **Structure**: Uses a `@dataclass` called `Config`.
- **Features**: Stores agent identity (name, description), default prompts, LLM constraints (max_tokens), and behavioral settings (max_iterations).
- **Validation (`__post_init__`)**: Ensures name is provided and integer settings are valid (> 0).
- **Flow and Connections**: This acts as a central repository for agent state and settings, consumed by `BaseAgent` to govern how it interacts with the LLM and the environment.

## File: llms/groqclient.py
The Groq LLM interface client.

### Code Breakdown
- **Initialization**: Initializes the `Groq` client, sets the model, and configures the `max_tokens` limit.
- **generate() method**: Sends messages to the Groq API (system and user content) and returns the text response from the model.
- **Flow and Connections**: Similar to `GeminiClient`, this is an interchangeable LLM provider. It implements `BaseLLM` and is prepared for use within `BaseAgent` as a substitute or companion to the Gemini implementation.

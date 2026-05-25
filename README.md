# Khwarizm - AI Agent Framework

## Overview
Khwarizm is a minimalist, production-inspired AI Agent Framework built entirely from scratch using core Object-Oriented Programming principles in Python. It wraps stateless Large Language Models (LLMs) into intelligent, autonomous agents capable of persistent memory, tool use, and multi-step reasoning.

---

## The Problem We Solve
Large Language Models are stateless. Every time you call them, they forget everything. They cannot:
- Remember previous conversations
- Take actions in the real world
- Reason through multi-step problems
- Use external tools like calculators or file systems

**Khwarizm solves all of these problems.**

---

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

---

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

---

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

---

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

---

## Memory System

Khwarizm has two types of memory working simultaneously:

| | Short Term Memory | Long Term Memory |
|--|------------------|-----------------|
| **Storage** | Python List (RAM) | JSON File (Disk) |
| **Lives** | Current session only | Forever |
| **Dies when** | Program closes | Never |
| **Analogy** | Human working memory | Human long term memory |

---

## Key Concepts Explained

---

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

---

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

---

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

---

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

---

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

---

#### `available_tools` property
```python
@property
def available_tools(self) -> list:
    return self.registry.list_tools()
```

Returns a clean list of tool names without 
exposing the internal Registry object.

---

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

---

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

---

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

---

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

---

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

---

## Multi-Agent Workflow

Because `BaseAgent.run()` takes text in and returns text out, agents can be chained together using pure Python:

```python
# Agent 1 writes a poem
writer_output = writer_agent.run("Write a poem about AI")

# Agent 2 critiques what Agent 1 wrote
critic_output = critic_agent.run(writer_output)
```

No special framework needed. Just Python variables.

---

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

---

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

---

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

---

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

---

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

---

## What We Would Add Next

1. **SupervisorAgent** - An agent that manages other agents and routes tasks between them
2. **Streamlit Web UI** - A browser-based chat interface for the framework
3. **WebSearchTool** - Live internet access via DuckDuckGo or Wikipedia API
4. **Python Logging** - Replace print statements with proper log levels
5. **Memory Summarization** - Compress long term memory using LLM summaries to prevent context overflow

---

## Authors
Built by Faseeh ur Rehman and Huzaifa Imran as part of an OOP and AI Agents learning project.
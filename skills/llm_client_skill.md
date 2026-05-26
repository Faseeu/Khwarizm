# Guide to Creating LLM Clients for the Khwarizm Architecture

To create a functional LLM client that integrates with the existing system, you must inherit from the `BaseLLM` abstract class and adhere to the following requirements:

## 1. Class Structure
Every LLM client must be implemented as a class that inherits from `BaseLLM` (located in `llms/basellm.py`). This ensures compatibility with the agent's LLM orchestration.

## 2. Interface Requirements
Each client must implement:
- **`__init__`**: Handle secure credential retrieval (e.g., from environment variables) and SDK initialization.
- **`generate(system_prompt: str, user_prompt: str) -> str`**: The core method that maps the agent's inputs to the specific provider's API request format.

## 3. Integration
1. Define the class in the `llms/` directory.
2. Ensure the class overrides the abstract methods defined in `BaseLLM`.
3. Use standard error handling to ensure failures return a descriptive string rather than crashing the execution flow.

## 4. Execution Protocol
Clients must be stateless. They are initialized once and utilized for message generation based on the current context provided by the agent.

# Example: Building an LLM Client

To create an LLM client, follow this pattern:

1. **Inheritance**: Inherit from `BaseLLM`.
2. **Implementation**:
```python
import os
from llms.basellm import BaseLLM

class ExampleLLMClient(BaseLLM):
    def __init__(self):
        self.api_key = os.environ.get("EXAMPLE_API_KEY")
        # Initialize your SDK here
        
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            # Construct payload and call provider API
            return "Generated response from LLM"
        except Exception as e:
            return f"Error: LLM provider failed: {str(e)}"
```

This pattern ensures that the system remains extensible to any LLM provider while maintaining a strict, predictable interface.
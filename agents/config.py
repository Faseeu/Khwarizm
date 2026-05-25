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
        
        



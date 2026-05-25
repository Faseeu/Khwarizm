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


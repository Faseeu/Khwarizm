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
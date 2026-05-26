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
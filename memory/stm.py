from collections import deque
from memory.memory import BaseMemory

class ShortTermMemory(BaseMemory):

    def __init__(self, max_entries: int = 50):
        self.__history = deque(maxlen=max_entries)

    def add_entry(self, role: str, content: str) -> None:
        self.__history.append({"role": role, "content": content})

    def get_history(self) -> list:
        return list(self.__history)

    def clear(self) -> None:
        self.__history.clear()
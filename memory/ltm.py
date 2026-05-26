import json
import os
from collections import deque
from memory.memory import BaseMemory

class LongTermMemory(BaseMemory):

    def __init__(self, agent_name: str, max_entries: int = 100):
        self.__file_path = f"{agent_name}_memory.json"
        self.__max_entries = max_entries
        self.__history = deque(
            self.__load_from_file(),
            maxlen=max_entries
        )

    def add_entry(self, role: str, content: str) -> None:
        self.__history.append({"role": role, "content": content})
        self.__save_to_file()

    def get_history(self) -> list:
        return list(self.__history)

    def clear(self) -> None:
        self.__history.clear()
        self.__save_to_file()

    def __save_to_file(self) -> None:
        try:
            with open(self.__file_path, "w") as f:
                json.dump(list(self.__history), f, indent=4)
        except Exception as e:
            print(f"Warning: Could not save memory. Error: {e}")

    def __load_from_file(self) -> list:
        if not os.path.exists(self.__file_path):
            return []
        try:
            with open(self.__file_path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Warning: Memory file unreadable. Starting fresh. Error: {e}")
            return []
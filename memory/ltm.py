import json
import os
from collections import deque
from memory.memory import BaseMemory


class LongTermMemory(BaseMemory):
    """
    Persistent memory that survives across sessions.
    Stored as a JSON file on disk.
    
    Uses a deque so the rolling window is enforced automatically.
    When loading old data, the deque trims it to max_entries
    immediately so stale oversized files are cleaned up on first load.
    
    Files are saved to memory_store/ folder to keep the root clean.
    """

    STORAGE_DIR = "memory_store"

    def __init__(self, agent_name: str, max_entries: int = 100):
        """
        Args:
            agent_name:  Used as the filename key. Keep consistent per agent.
            max_entries: Rolling window size. Oldest entries dropped when exceeded.
        """
        os.makedirs(self.STORAGE_DIR, exist_ok=True)
        self.__file_path = os.path.join(self.STORAGE_DIR, f"{agent_name}_memory.json")
        self.__max_entries = max_entries
        self.__history: deque = deque(
            self.__load_from_file(),
            maxlen=max_entries
        )
        print(f"[LTM] Initialized. Will save to: {os.path.abspath(self.__file_path)}")


    def add_entry(self, role: str, content: str) -> None:
        """Add a message and immediately persist to disk."""
        self.__history.append({"role": role, "content": content})
        self.__save_to_file()
        print(f"[LTM] Entry added. Total entries: {len(self.__history)}")

    def get_history(self) -> list[dict]:
        """Return a copy of history as a plain list."""
        return list(self.__history)

    def clear(self) -> None:
        """Wipe memory in RAM and on disk."""
        self.__history.clear()
        self.__save_to_file()

    def __save_to_file(self) -> None:
        try:
            with open(self.__file_path, "w") as f:
                json.dump(list(self.__history), f, indent=4)
            print(f"[LTM] Saved to {os.path.abspath(self.__file_path)}")
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

    def __len__(self) -> int:
        return len(self.__history)

    def __repr__(self) -> str:
        return (
            f"LongTermMemory(agent='{os.path.basename(self.__file_path)}', "
            f"entries={len(self)}, max={self.__max_entries})"
        )
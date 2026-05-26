from collections import deque
from memory.memory import BaseMemory


class ShortTermMemory(BaseMemory):
    """
    In-RAM memory for the current session only.
    Dies when the process ends.
    Uses a deque with maxlen so old entries are automatically
    dropped when the limit is hit. No manual trimming needed.
    """

    def __init__(self, max_entries: int = 50):
        """
        Args:
            max_entries: Maximum entries to keep in RAM.
                         When exceeded, oldest entry is dropped automatically.
        """
        self.__history: deque = deque(maxlen=max_entries)

    def add_entry(self, role: str, content: str) -> None:
        """Add a message to memory. Oldest entry auto-dropped if at capacity."""
        self.__history.append({"role": role, "content": content})

    def get_history(self) -> list[dict]:
        """Return a copy of history. Copy protects internal deque from mutation."""
        return list(self.__history)

    def clear(self) -> None:
        """Wipe all entries."""
        self.__history.clear()

    def __len__(self) -> int:
        return len(self.__history)

    def __repr__(self) -> str:
        return f"ShortTermMemory(entries={len(self)}, max={self.__history.maxlen})"
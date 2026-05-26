from abc import ABC, abstractmethod

class BaseMemory(ABC):

    @abstractmethod
    def add_entry(self, role: str, content: str) -> None:
        pass

    @abstractmethod
    def get_history(self) -> list:
        """Return raw history list. Must return a copy, not the live list."""
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    def get_context(self) -> str:
        """Shared by all subclasses. Override only if you need different formatting."""
        history = self.get_history()
        if not history:
            return ""
        return "".join(
            f"{entry['role']}: {entry['content']}\n"
            for entry in history
        )
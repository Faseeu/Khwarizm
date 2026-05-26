import os
from tools.basetool import BaseTool


class DirectoryWatcherTool(BaseTool):
    """
    Lists the directory tree of a given path.
    Recursive up to max_depth levels deep.
    """
    name = "directory_watcher"
    description = "Returns a recursive directory tree of a given path."
    parameters = {
        "path": "The directory path to inspect. Use '.' for current directory.",
        "max_depth": "How deep to recurse. Default is 2. Max recommended is 4."
    }

    def run(self, parameters: dict) -> str:
        path = parameters.get("path", ".").strip() or "."
        try:
            max_depth = int(parameters.get("max_depth", 2))
        except (ValueError, TypeError):
            max_depth = 2

        if not os.path.exists(path):
            return f"Error: Path '{path}' does not exist."
        if not os.path.isdir(path):
            return f"Error: '{path}' is not a directory."

        lines: list[str] = []
        self.__walk(path, lines, depth=0, max_depth=max_depth)
        return "\n".join(lines) if lines else "Directory is empty."

    def __walk(self, path: str, lines: list, depth: int, max_depth: int) -> None:
        """Recursively walk directory and build the tree lines."""
        if depth > max_depth:
            return
        try:
            entries = sorted(os.listdir(path))
        except PermissionError:
            lines.append("  " * depth + "[Permission Denied]")
            return

        for entry in entries:
            indent = "  " * depth
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                lines.append(f"{indent}📁 {entry}/")
                self.__walk(full_path, lines, depth + 1, max_depth)
            else:
                lines.append(f"{indent}📄 {entry}")
from tools.basetool import BaseTool
import os

class DirectoryWatcherTool(BaseTool):
    def __init__(self):
        self.name = "directory_watcher"
        self.description = "Lists files in a directory to keep track of changes."
        self.parameters = {
            "path": "The path of the directory to list."
        }

    def run(self, parameters: dict) -> str:
        path = parameters.get("path", ".")
        try:
            files = os.listdir(path)
            return f"Files in {path}: {', '.join(files)}"
        except Exception as e:
            return f"Error accessing directory: {str(e)}"
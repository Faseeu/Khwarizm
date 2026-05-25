from tools.basetool import BaseTool

import os

class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file in the current working directory only."
    parameters = {
        "filename": "The name of the file to write. Example: result.txt",
        "content": "The full text content to write into the file."
    }

    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()
            content = parameters.get("content", "").strip()

            if not filename:
                return "Error: filename parameter is missing."

            # Prevent path traversal attacks
            safe_path = os.path.realpath(os.path.join(os.getcwd(), filename))
            if not safe_path.startswith(os.getcwd()):
                return "Error: Writing outside the working directory is not allowed."

            # Create subdirectories if needed (safely)
            os.makedirs(os.path.dirname(safe_path), exist_ok=True) \
                if os.path.dirname(safe_path) else None

            with open(safe_path, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"

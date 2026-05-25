from tools.basetool import BaseTool

class FileReaderTool(BaseTool):
    name = "file_reader"
    description = "Reads and returns the content of a file."
    parameters = {
        "filename": "The name of the file to read. Example: result.txt"
    }

    def run(self, parameters: dict) -> str:
        try:
            filename = parameters.get("filename", "").strip()

            if not filename:
                return "Error: filename parameter is missing."

            with open(filename, "r") as f:
                content = f.read()
            return f"Content of {filename}:\n{content}"
        except FileNotFoundError:
            return f"Error: File '{filename}' not found."
        except Exception as e:
            return f"Error reading file: {e}"
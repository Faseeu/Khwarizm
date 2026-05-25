from tools.basetool import BaseTool

class FileWriterTool(BaseTool):
    name = "file_writer"
    description = "Writes content to a file on the local filesystem."
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

            with open(filename, "w") as f:
                f.write(content)
            return f"Successfully wrote to {filename}"
        except Exception as e:
            return f"Error writing file: {e}"
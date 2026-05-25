from tools.basetool import BaseTool
import subprocess

class TerminalExecutorTool(BaseTool):
    def __init__(self):
        self.name = "terminal_executor"
        self.description = "Executes shell commands after explicit user confirmation."
        self.parameters = {
            "command": "The shell command to be executed."
        }

    def run(self, parameters: dict) -> str:
        command = parameters.get("command", "")
        print(f"The following command will be executed: {command}. Proceed? (y/n)")
        choice = input().strip().lower()
        
        if choice == 'y':
            try:
                result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Command failed: {e.output}"
        else:
            return "Command execution cancelled by user."

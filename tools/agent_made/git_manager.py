from tools.basetool import BaseTool
import subprocess

class GitManagerTool(BaseTool):
    def __init__(self):
        self.name = "git_manager"
        self.description = "Provides a safe interface to run 'git status' or 'git log' to track project changes."
        self.parameters = {
            "command": "The git command to execute (e.g., 'status', 'log -n 5')."
        }

    def run(self, parameters: dict) -> str:
        cmd_arg = parameters.get("command", "status")
        full_command = f"git {cmd_arg}"
        print(f"The following git command will be executed: {full_command}. Proceed? (y/n)")
        choice = input().strip().lower()
        
        if choice == 'y':
            try:
                result = subprocess.check_output(full_command, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Git command failed: {e.output}"
        else:
            return "Git command execution cancelled by user."
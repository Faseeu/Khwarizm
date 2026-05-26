from tools.basetool import BaseTool
import subprocess
import os
import shutil

class LightPythonRunnerTool(BaseTool):

    name = "light_python_runner"
    description = "Executes python files in a clean, ephemeral virtual environment that is deleted immediately after execution."
    parameters = {
        "filepath": "The path to the python file to execute."
    }

    def run(self, parameters: dict) -> str:
        filepath = parameters.get("filepath", "")
        venv_dir = ".ephemeral_venv"
        
        # Cleanup if old one exists
        if os.path.exists(venv_dir):
            shutil.rmtree(venv_dir)
            
        cmd = f"python3 -m venv {venv_dir} && {venv_dir}/bin/python3 {filepath}"
        
        print(f"The following ephemeral python execution will be run: {cmd}. Proceed? (y/n)")
        choice = input().strip().lower()
        
        if choice == 'y':
            try:
                result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
                return result
            except subprocess.CalledProcessError as e:
                return f"Execution failed: {e.output}"
            finally:
                if os.path.exists(venv_dir):
                    shutil.rmtree(venv_dir)
        else:
            return "Execution cancelled by user."
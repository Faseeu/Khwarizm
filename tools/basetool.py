from abc import ABC,abstractmethod

class BaseTool(ABC):

    def __init__(self):
        name: str
        description: str
        parameters: dict={}


        @abstractmethod
        def run(self, parameters: dict) -> str:
            """The method called by the agent to run a tool"""
            pass


    def get_schema(self) -> str:
        """Builds the XML schema shown to the LLM"""
        params_xml = ""
        for param_name, param_desc in self.parameters.items():
            params_xml += f"\n        <{param_name}>({param_desc})</{param_name}>"

        return (
            f"<tool>\n"
            f"  <tool_name>{self.name}</tool_name>\n"
            f"  <description>{self.description}</description>\n"
            f"  <parameters>{params_xml}\n  </parameters>\n"
            f"</tool>"
        )
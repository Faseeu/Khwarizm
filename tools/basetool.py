from abc import ABC,abstractmethod

class BaseTool(ABC):


    name: str
    description: str
    parameters: dict={}


    @abstractmethod
    def run(self, parameters: dict) -> str:
        """
        Execute the tool with the given parameters.
        
        Args:
            parameters: Dict of parameter names to values.
                        Keys must match what's defined in self.parameters.
        
        Returns:
            Result string. Always returns a string, never raises.
        """
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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
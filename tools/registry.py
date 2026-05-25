from tools.basetool import BaseTool

class ToolRegistry:
    def __init__(self):
        self.__tools = {}

    def register(self, tool: BaseTool):
        self.__tools[tool.name] = tool
        print(f"Registered tool: {tool.name}")

    def get_tool(self, name: str) -> BaseTool:
        return self.__tools.get(name)

    def get_descriptions(self) -> str:
        """Returns full XML schemas for all tools"""
        schemas = []
        for tool in self.__tools.values():
            schemas.append(tool.get_schema())
        return "\n\n".join(schemas)

    def list_tools(self) -> list:
        return list(self.__tools.keys())
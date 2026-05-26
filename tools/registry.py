from tools.basetool import BaseTool

class ToolRegistry:

    def __init__(self):
        self.__tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        if tool.name in self.__tools:
            print(f"Warning: Tool '{tool.name}' already registered. Overwriting.")
        self.__tools[tool.name] = tool

    def get_tool(self, name: str) -> BaseTool:
        return self.__tools.get(name)

    def get_descriptions(self) -> str:
        return "\n\n".join(tool.get_schema() for tool in self.__tools.values())

    def list_tools(self) -> list:
        return list(self.__tools.keys())

    def __len__(self) -> int:
        return len(self.__tools)
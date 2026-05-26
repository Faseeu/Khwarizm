from tools.basetool import BaseTool


class ToolRegistry:
    """
    Stores and manages all tools available to an agent.
    
    Internally uses a dictionary for O(1) lookup by tool name.
    Tools are registered once at agent startup and looked up
    every time the LLM decides to call one.
    """

    def __init__(self):
        self.__tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        """
        Register a tool. If a tool with the same name exists, warns and overwrites.
        
        Args:
            tool: Any object that inherits from BaseTool.
        """
        if tool.name in self.__tools:
            print(f"Warning: Tool '{tool.name}' already registered. Overwriting.")
        self.__tools[tool.name] = tool

    def get_tool(self, name: str) -> BaseTool | None:
        """
        Retrieve a tool by name. Returns None if not found.
        The agent checks for None and returns an error to the LLM.
        """
        return self.__tools.get(name)

    def get_descriptions(self) -> str:
        """
        Build the full XML schema block for all registered tools.
        This is injected into the system prompt so the LLM knows
        what tools exist and how to call them.
        """
        return "\n\n".join(tool.get_schema() for tool in self.__tools.values())

    def list_tools(self) -> list[str]:
        """Return a list of all registered tool names."""
        return list(self.__tools.keys())

    def __len__(self) -> int:
        return len(self.__tools)

    def __repr__(self) -> str:
        return f"ToolRegistry(tools={self.list_tools()})"
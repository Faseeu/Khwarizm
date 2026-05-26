from agents.config import Config
from llms import BaseLLM
from tools import ToolRegistry
from memory.stm import ShortTermMemory
from memory.ltm import LongTermMemory
import xml.etree.ElementTree as ET

class BaseAgent:
    def __init__(self,
                name,
                llm:BaseLLM,
                system_prompt: str = "You are a helpful AI assistant", 
                
                tools: list = None
                ):
        
        self.llm = llm

        self.registry = ToolRegistry()
        tools = tools or []
        # THE LOOP 
        # Which automates the work of resgistering the TOOLS manually
        for tool in tools:
            self.registry.register(tool)

        # This is basically a prompt that tells the llm what tools it has
        if tools:
            tool_schemas = self.registry.get_descriptions()
            system_prompt = (
                f"{system_prompt}\n\n"
                f"You have access to these tools:\n"
                f"{tool_schemas}\n\n"
                f"STRICT RULES:\n"
                f"CRITICAL: Only use ONE tool per response. Wait for the tool result before taking your next step.\n"
                f"1. Use ONE tool per response. No exceptions.\n"
                f"2. After using a tool,Stop. wait for the result before continuing. Do not write anything else.\n"
                f"3. If you use more than one tool in a single response, I will stop the conversation and you will fail the task.\n\n"
                f"4. NEVER call the same or different tool twice in one response.\n"
                f"5. You MUST use tools when the task requires them.\n\n"
                f"To use a tool, respond EXACTLY in this XML format:\n\n"
                f"<tool_use>\n"
                f"  <tool_name>tool_name_here</tool_name>\n"
                f"  <parameters>\n"
                f"    <param_name>value here</param_name>\n"
                f"  </parameters>\n"
                f"</tool_use>"
            )

        # THE CONFIG
        self.config = Config(
            name=name,
            description="Agent",
            system_prompt=system_prompt,
        )

        # Memory 
        # The Memory part of the agent
        # Truly automatic  
        self.__base_system_prompt = system_prompt
        self.__short_term = ShortTermMemory(max_entries=self.config.max_stm_entries)
        self.__long_term = LongTermMemory(
            agent_name=name,
            max_entries=self.config.max_ltm_entries
            )

    @property
    def name(self) -> str:
        # agent's name
        return self.config.name
    
    @property
    def description(self) -> str:
        # agent's description
        return self.config.description

    @property
    def system_prompt(self) -> str:
        # system prompt
        return self.config.system_prompt

    @property
    def tools(self) -> list:
        # list of tool names
        return self.registry.list_tools()
    

    def run(self, user_input: str) -> str:

        self.__short_term.add_entry(role="user", content= user_input)
        self.__long_term.add_entry(role="user", content= user_input)


        iterations = 0
        max_iters = self.config.max_iterations

        print(f"Starting: {self.config.name} \n{self.config.name} is thinking...")
        

        while iterations < max_iters:
            iterations += 1
            print(f"  [Loop {iterations}/{max_iters}] Agent is thinking...")

            #  Build context from BOTH memories

            long_term_context = self.__long_term.get_context()
            short_term_context = self.__short_term.get_context()

            #  Combine them into one prompt
            full_context = (
                f"Past Conversations:\n{long_term_context}\n\n"
                f"Current Session:\n{short_term_context}"
            )
            
            # print("\n--- SYSTEM PROMPT ---")
            # print(self.config.system_prompt)
            # print("--- END SYSTEM PROMPT ---\n")


            response = self.llm.generate(
                system_prompt=self.__base_system_prompt,
                user_prompt=full_context
            )

            if response.startswith("Error: LLM API failed"):
                print("  -> Critical LLM Error encountered.")
                return response
            
            
            if "<think>" in response and "</think>" in response:
                response = response.split("</think>")[-1].strip()

        # Check if LLM decided to use a tool
            if "<tool_use>" in response:
                tool_note = self.__handle_tool_call(response)

                self.__short_term.add_entry(
                    role="assistant",
                    content=response
                )
                self.__short_term.add_entry(
                    role="tool",
                    content=tool_note
                )
                continue

             # Save to both memories
            self.__short_term.add_entry(role="assistant", content=response)
            self.__long_term.add_entry(role="assistant", content=response)
            
            return response if response else "Error: Agent reached max iterations without a final answer."
    def __repr__(self) -> str:
                return (
                    f"BaseAgent(name='{self.name}', "
                    f"tools={self.tools}, "
                    f"stm={self.__short_term}, "
                    f"ltm={self.__long_term})"
                )
    
    def __handle_tool_call(self, response: str) -> str:
        try:
            start = response.find("<tool_use>")
            end = response.find("</tool_use>") + len("</tool_use>")
            xml_block = response[start:end]

            root = ET.fromstring(xml_block)

            # Extract tool name
            tool_name_el = root.find("tool_name")
            if tool_name_el is None:
                return "Error: No tool_name found in XML."
            tool_name = tool_name_el.text.strip()

            parameters = {}
            params_el = root.find("parameters")
            if params_el is not None:
                for param in params_el:
                    parameters[param.tag] = param.text.strip() if param.text else ""

            print(f"  -> Tool: {tool_name} | Parameters: {parameters}")

            # Fetch the tool from registry
            tool = self.registry.get_tool(tool_name)
            if not tool:
                return f"Error: Unknown tool '{tool_name}'. Available: {self.registry.list_tools()}"

            # Run the tool with the clean dictionary
            result = tool.run(parameters)
            return f"Tool '{tool_name}' returned: {result}"

        except ET.ParseError as e:
            return f"Error: Could not parse XML tool call. Details: {e}"
        except Exception as e:
            return f"Error during tool execution: {e}"


    def clear_memory(self):
        self.__short_term.clear()
        self.__long_term.clear()
        print(f"[{self.name}] Memory cleared.")
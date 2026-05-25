# from llms.groqclient import GroqClient
# from llms.geminiclient import GeminiClient
# from tools.calculator import CalculatorTool
# from tools.filewriter import FileWriterTool
# from tools.filereader import FileReaderTool
# from agents.baseagent import BaseAgent
from utils.chat_ui import start_terminal_chat

# if __name__ == "__main__":

#     # 1. Create the LLM
#     groq_llm = GroqClient(model="llama-3.3-70b-versatile")


#     # 2. Create the Agent with tools
#     agent = BaseAgent(
#         name="SmartBot",
#         llm=gemini_llm,
#         system_prompt= """
#         Be a helpful assistant who always always uses the tools given to him. 
#         Never do a task without using the apppropriate tools. 
#         You have all the appropriate tools at your disposal to perfrom the tasks i ask of you.
#         Always try to reason everything yourself.
#         Try your best not to bother user.
#         Create plans to perform the tasks.
#         Also at the end of each task try to double check if it was properly fullfilled or not. 
#         """,
#         tools=[CalculatorTool(),FileReaderTool(),FileWriterTool()]
#     )

#     print("\n" + "=" * 40)
#     print("TEST 2: Tool needed")
#     print("=" * 40)
# #     response2 = agent.run("""
# #     🌀 SYSTEM OVERRIDE: PROJECT HIDDEN GEM 🌀

# # Agent, your framework is entering the **Anime Recommendation Gauntlet**.  
# # Your mission: populate three classified dossiers, then unleash a fourth wild-card category that breaks the genre matrix.

# # ---

# # 📁 DOSSIER 1: `action`  
# # Compile the absolute GOATed action anime—titles with timelines so beautifully convoluted they require a whiteboard, and stories that hit harder than a final-form scream. Save the list to a file named **`action`**.

# # 📁 DOSSIER 2: `psychological`  
# # Infiltrate the deep cuts. I need **5 criminally underrated psychological anime** that are:
# # - Motivational enough to make me run through a wall,
# # - Political enough to start a debate club,
# # - Obscure enough that even seasoned weebs reply, *"Never heard of it."*  
# # Drop these into **`psychological`**.

# # 📁 DOSSIER 3: `most motivational anime`  
# # Uncover **5 motivational masterpieces** flying completely under the radar. Not the mainstream hype trains—actual underground bangers that rebuild your soul episode by episode. Write these to **`most motivational anime`**.

# # 🎲 DOSSIER 4: `[REDACTED]`  
# # Finally, deploy the wildcard. Create **one additional file** with a category so specific, so dangerously niche, that it feels like it was tailor-made for my brain. Make me fall in love with something I didn’t know existed.

# # ---

# # Execute with maximum flair. Framework stress-test: **ACTIVE**. ⚡
# #     """)
# #     print(response2)
#     start_terminal_chat(agent)


#     # # TEST THE PROPERTIES:
#     # print("--- AGENT INFO ---")
#     # print(f"Name: {agent.name}")                
#     # print(f"Tools: {agent.tools}")     
#     # print(f"Prompt: {agent.system_prompt}")      
#     # print("------------------")


from llms.geminiclient import GeminiClient
from tools.calculator import CalculatorTool
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent
from tools.agent_made.terminal_executor import TerminalExecutorTool


if __name__ == "__main__":
    
    llm = GeminiClient(model="gemini-3.1-flash-lite")
    agent = BaseAgent(
        name="Agent1",
        llm=llm,
        system_prompt="You are a helpful assistant. Always use tools for math and files. Always use tools. Never try to solve any math eq internally",
        tools=[CalculatorTool(), FileWriterTool(), FileReaderTool(),TerminalExecutorTool()]
    )

    # Test multi-parameter tool call
    # response = agent.run("""
    # Study the whole of tools directory
    # and create for yourself a terminal usage tool 
    # but it should have feature to show to the user
    # what command is going to be ran 
    # and ask him yes for y and no for n
    # """)
    start_terminal_chat(agent)

    print("\nFinal Answer:")
    # print(response)


        # "Calculate 1234 multiplied by 5678. "
        # "Then save the result to a file called answer.txt. "
        # "Then read the file back."
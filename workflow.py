from llms.geminiclient import GeminiClient
from tools.filewriter import FileWriterTool
from tools.filereader import FileReaderTool
from agents.baseagent import BaseAgent

llm = GeminiClient(model="gemini-3.1-flash-lite")

# Agent 1: The Writer
writer = BaseAgent(
    name="Writer",
    llm=llm,
    system_prompt="You are a creative writer. Write what the user asks and nothing else. Also use tools",
    tools=[FileWriterTool()]
)

# Agent 2: The Critic
critic = BaseAgent(
    name="Critic",
    llm=llm,
    system_prompt="You are a harsh critic. Read what is given to you and give brutal feedback. Also use tools",
    tools=[FileReaderTool()]
)

poet= BaseAgent(
    name="Poet",
    llm=llm,
    system_prompt="Write a poem in a file",
    tools=[FileReaderTool()]
)
print("Step 1: Writer writes a poem...")
writer_output = writer.run("Write a short poem about AI and save it to poem.txt")
poetOutput = poet.run("Gimme the poems")
print("\nStep 2: Critic reviews the poem...")
critic_output = critic.run("Read poem.txt and another poem file and crush their dreams and give me harsh feedback on it")

print("\nCritic's Verdict:")
print(critic_output)
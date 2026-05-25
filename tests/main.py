from Khwarizm.baseagent import BaseAgent
from Khwarizm.clients import GroqClient

# test1[9MAY]
if __name__ == "__main__":
    groqclient = GroqClient(
        model="openai/gpt-oss-120b"
    )

    groq_agent = BaseAgent(
        name="Future AI",
        llm=groqclient,
        #system_prompt="You are a helpful AI but you must speak like a dictator from the science fiction future"
    )

    user = "Explain what is it like to own a drone industry in the future"

    print(f"User: {user}")

    response = groq_agent.run(user)

    print(f"{groq_agent.config.name} Reply: ")
    print(response)
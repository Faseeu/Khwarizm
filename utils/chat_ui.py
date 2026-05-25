# utils/chat_ui.py

def start_terminal_chat(agent):
    print("=" * 50)
    print(f"Starting chat with {agent.name}. Type 'exit' to quit.")
    print("=" * 50)
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation...")
            break
            
        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
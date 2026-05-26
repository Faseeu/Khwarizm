def start_terminal_chat(agent) -> list:
    print("=" * 50)
    print(f"Chat with {agent.name} | Tools: {agent.tools}")
    print("Type 'exit' to quit. Type 'clear' to reset memory.")
    print("=" * 50)

    history = []

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSession ended.")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit","e","q"):
            print("Ending conversation...")
            break

        if user_input.lower() == "clear":
            agent.clear_memory()
            print("[Memory cleared]")
            continue

        response = agent.run(user_input)
        print(f"\n{agent.name}: {response}")
        history.append({"user": user_input, "agent": response})

    return history
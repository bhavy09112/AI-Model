"""
Main entry point for the AI Hackathon Model
"""

from groq_client import GroqClient


def main():
    """Main function to demonstrate Groq integration"""
    try:
        # Initialize Groq client
        client = GroqClient()
        # Example: Get a simple completion and keep conversation history
        messages = []
        prompt = input("How can I help you? \n")
        response = client.get_completion(prompt)
        print(f"Assistant: {response}\n")

        # Save initial exchange
        messages.append({"role": "user", "content": prompt})
        messages.append({"role": "assistant", "content": response})

        # Enter interactive loop allowing replies to a particular message
        while True:
            print("Conversation history:")
            for i, m in enumerate(messages):
                preview = m['content']
                if len(preview) > 120:
                    preview = preview[:117] + '...'
                print(f"[{i}] {m['role']}: {preview}")

            choice = input("Reply to message index, 'n' to send a new message, or 'q' to quit: ")
            if choice.strip().lower() in ("q", "quit"):
                print("Exiting chat.")
                break

            if choice.strip().lower() == 'n':
                user_text = input("Your message: ")
                messages.append({"role": "user", "content": user_text})
            else:
                try:
                    idx = int(choice)
                except ValueError:
                    print("Please enter a valid index, 'n', or 'q'.")
                    continue

                if idx < 0 or idx >= len(messages):
                    print("Index out of range. Try again.")
                    continue

                target = messages[idx]
                user_text = input(f"Your reply to [{idx}] ({target['role']}): ")
                # Quote the target message so the model understands which message is being replied to
                quoted = f">>> Quoting {target['role']} message (index {idx}):\n{target['content']}\n---\n{user_text}"
                messages.append({"role": "user", "content": quoted})

            # Get assistant reply using full conversation history
            chat_response = client.get_chat_response(messages)
            print(f"Assistant: {chat_response}\n")
            messages.append({"role": "assistant", "content": chat_response})
        
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()

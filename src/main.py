"""
Main entry point for the AI Hackathon Model
"""

from groq_client import GroqClient


def main():
    """Main function to demonstrate Groq integration"""
    try:
        # Initialize Groq client
        client = GroqClient()
        
        # Example: Get a simple completion
        prompt = "What is the capital of France?"
        print(f"Prompt: {prompt}")
        response = client.get_completion(prompt)
        print(f"Response: {response}\n")
        
        # Example: Chat conversation
        messages = [
            {"role": "user", "content": "Hello, what can you do?"},
        ]
        print(f"User: {messages[0]['content']}")
        chat_response = client.get_chat_response(messages)
        print(f"Assistant: {chat_response}\n")
        
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()

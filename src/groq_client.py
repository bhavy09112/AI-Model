"""
Groq API Client Module
Handles interactions with Groq API for AI model inference
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class GroqClient:
    """Client for interacting with Groq API"""
    
    def __init__(self):
        """Initialize Groq client with API key from environment"""
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.client = Groq(api_key=self.api_key)
    
    def get_completion(self, prompt: str, temperature: float = 0.7, max_tokens: int = 1000) -> str:
        """
        Get a completion from Groq API
        
        Args:
            prompt: The input prompt
            temperature: Controls randomness (0-2)
            max_tokens: Maximum tokens in response
            
        Returns:
            The model's response text
        """
        try:
            message = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return message.choices[0].message.content
        except Exception as e:
            print(f"Error getting completion: {e}")
            raise
    
    def get_chat_response(self, messages: list, temperature: float = 0.7, max_tokens: int = 1000) -> str:
        """
        Get a chat response from Groq API
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            temperature: Controls randomness (0-2)
            max_tokens: Maximum tokens in response
            
        Returns:
            The model's response text
        """
        try:
            response = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error getting chat response: {e}")
            raise

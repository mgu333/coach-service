"""OpenAI service module for generating AI-powered coaching responses.

This module provides an interface to OpenAI's GPT models for generating
personalized coaching messages with conversation history and context awareness.
"""

import openai
from typing import List, Dict, Optional, Any


class OpenAIService:
    """Service class for interacting with OpenAI's GPT models.
    
    This class manages API communication with OpenAI and handles the generation
    of coaching responses based on user input, context, and conversation history.
    
    Attributes:
        api_key (str): OpenAI API authentication key.
        model (str): The GPT model to use (default: 'gpt-4').
        system_prompt (str): The base system prompt that defines the coach's personality.
    
    Example:
        >>> service = OpenAIService(api_key="sk-...")
        >>> response = service.generate_coaching_response(
        ...     message="I'm feeling unmotivated today",
        ...     context={"mood": "low"}
        ... )
    """
    
    def __init__(self, api_key: str, model: str = "gpt-4") -> None:
        """Initialize the OpenAI service with API credentials.
        
        Args:
            api_key (str): OpenAI API key for authentication.
            model (str, optional): GPT model identifier. Defaults to "gpt-4".
        
        Note:
            The API key is set globally for the openai module upon initialization.
        """
        self.api_key: str = api_key
        self.model: str = model
        openai.api_key = api_key
        
        # Define the coach's personality and behavioral guidelines
        self.system_prompt: str = """You are an empathetic and motivating morning coach. 
Your role is to help people start their day positively, set intentions, 
and overcome morning challenges. Be warm, encouraging, and practical.

Guidelines:
- Keep responses concise but meaningful (2-4 sentences)
- Be genuinely encouraging without being cheesy
- Ask follow-up questions to deepen engagement
- Provide actionable advice when appropriate
- Remember context from the conversation
"""
    
    def generate_coaching_response(
        self, 
        message: str, 
        context: Optional[Dict[str, Any]] = None,
        history: Optional[List[Dict[str, str]]] = None
    ) -> str:
        """Generate a personalized coaching response using OpenAI's GPT model.
        
        This method constructs a conversation context including system prompts,
        user context, conversation history, and the current message, then sends
        it to OpenAI for response generation.
        
        Args:
            message (str): The current user message to respond to.
            context (Optional[Dict[str, Any]], optional): Additional user context
                (e.g., mood, goals, preferences). Defaults to None.
            history (Optional[List[Dict[str, str]]], optional): Previous conversation
                interactions. Each dict should have 'user_message' and 'coach_response'
                keys. Only the last 5 interactions are used. Defaults to None.
        
        Returns:
            str: The generated coaching response from OpenAI.
        
        Raises:
            Exception: Returns an error message string if the API call fails,
                rather than raising the exception.
        
        Example:
            >>> response = service.generate_coaching_response(
            ...     message="I slept poorly last night",
            ...     context={"sleep_hours": 4},
            ...     history=[{
            ...         "user_message": "Good morning",
            ...         "coach_response": "Good morning! How are you feeling?"
            ...     }]
            ... )
        """
        # Initialize messages list with system prompt
        messages: List[Dict[str, str]] = [
            {"role": "system", "content": self.system_prompt}
        ]
        
        # Add context information if provided
        if context:
            context_str: str = f"User context: {context}"
            messages.append({"role": "system", "content": context_str})
        
        # Include recent conversation history (last 5 interactions)
        # This helps maintain conversation continuity and context awareness
        if history:
            for interaction in history[-5:]:
                messages.append({
                    "role": "user", 
                    "content": interaction.get('user_message', '')
                })
                messages.append({
                    "role": "assistant", 
                    "content": interaction.get('coach_response', '')
                })
        
        # Add the current user message
        messages.append({"role": "user", "content": message})
        
        try:
            # Call OpenAI API with configured parameters
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.8,  # Higher temperature for more creative/varied responses
                max_tokens=200     # Limit response length for conciseness
            )
            
            # Extract and return the generated message content
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            # Return user-friendly error message instead of raising exception
            # This ensures the application can gracefully handle API failures
            return f"I'm having trouble connecting right now. Let's try again! Error: {str(e)}"

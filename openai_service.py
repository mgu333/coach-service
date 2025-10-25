import openai
from typing import List, Dict, Optional

class OpenAIService:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.api_key = api_key
        self.model = model
        openai.api_key = api_key

        self.system_prompt = """You are an empathetic and motivating morning coach. 
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
        context: Optional[Dict] = None,
        history: Optional[List[Dict]] = None
    ) -> str:
        """Generate a coaching response using OpenAI"""

        messages = [{"role": "system", "content": self.system_prompt}]

        # Add context if provided
        if context:
            context_str = f"User context: {context}"
            messages.append({"role": "system", "content": context_str})

        # Add history (last 5 interactions)
        if history:
            for interaction in history[-5:]:
                messages.append({"role": "user", "content": interaction.get('user_message', '')})
                messages.append({"role": "assistant", "content": interaction.get('coach_response', '')})

        # Add current message
        messages.append({"role": "user", "content": message})

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0.8,
                max_tokens=200
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            return f"I'm having trouble connecting right now. Let's try again! Error: {str(e)}"

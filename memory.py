from datetime import datetime
from typing import List, Dict
from collections import defaultdict

class MemoryStore:
    """Simple in-memory storage for conversation history"""

    def __init__(self):
        self.conversations = defaultdict(list)
        self.max_history = 50  # Keep last 50 interactions per user

    def add_interaction(self, user_id: str, user_message: str, coach_response: str):
        """Store a conversation interaction"""
        interaction = {
            'timestamp': datetime.utcnow().isoformat(),
            'user_message': user_message,
            'coach_response': coach_response
        }

        self.conversations[user_id].append(interaction)

        # Trim history if too long
        if len(self.conversations[user_id]) > self.max_history:
            self.conversations[user_id] = self.conversations[user_id][-self.max_history:]

    def get_history(self, user_id: str) -> List[Dict]:
        """Retrieve conversation history for a user"""
        return self.conversations.get(user_id, [])

    def clear_history(self, user_id: str):
        """Clear conversation history for a user"""
        if user_id in self.conversations:
            del self.conversations[user_id]

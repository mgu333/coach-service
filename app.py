"""Flask application for AI coach service.

This module provides a webhook endpoint that receives coaching requests
and generates personalized coaching messages based on event type, context,
and desired message length.
"""

from typing import Any, Dict, Tuple
from flask import Flask, request, jsonify, Response
import os

app = Flask(__name__)


@app.get("/status")
def status() -> Response:
    """Health check endpoint.
    
    Returns:
        Response: JSON response with ok=True status.
    """
    return jsonify(ok=True)


@app.post("/coach")
def coach() -> Tuple[Response, int] | Response:
    """Main coaching endpoint that processes webhook requests.
    
    Validates the webhook secret, parses the request payload, and returns
    a personalized coaching message based on the event type and context.
    
    Request Headers:
        X-Auth: Webhook authentication secret.
    
    Request Body (JSON):
        event (str, optional): Type of event (e.g., 'morning', 'evening'). 
            Defaults to 'morning'.
        context (str, optional): Additional context for the coaching message.
            Defaults to empty string.
        len (str, optional): Desired message length ('short', 'medium', 'long').
            Defaults to 'short'.
    
    Returns:
        Response | Tuple[Response, int]: JSON response with coaching message,
            or error response with 401 status code if unauthorized.
    
    Example:
        >>> # POST /coach with X-Auth header
        >>> # Body: {"event": "morning", "context": "feeling tired", "len": "short"}
        >>> # Returns: {"event": "morning", "context": "feeling tired", ...}
    """
    # Verify webhook secret from environment variable
    secret: str | None = os.environ.get("COACH_WEBHOOK_SECRET")
    header: str = request.headers.get("X-Auth", "")
    
    if not secret or header != secret:
        return jsonify(error="unauthorized"), 401
    
    # Parse and validate request payload with defaults
    data: Dict[str, Any] = request.get_json(silent=True) or {}
    event: str = data.get("event", "morning")
    context: str = data.get("context", "")
    length: str = data.get("len", "short")
    
    # Placeholder response (replace with OpenAI call in production)
    # TODO: Integrate with OpenAI service for dynamic message generation
    response: Dict[str, str] = {
        "event": event,
        "context": context,
        "length": length,
        "coach_message": "Good morning — try a 2-minute breathing exercise and set one small intention for today."
    }
    
    return jsonify(response)


if __name__ == "__main__":
    # Get port from environment variable or default to 8080
    port: int = int(os.environ.get("PORT", 8080))
    # Run Flask app on all network interfaces
    app.run(host="0.0.0.0", port=port)

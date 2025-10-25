from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.get("/status")
def status():
    return jsonify(ok=True)

@app.post("/coach")
def coach():
    # Verify webhook secret
    secret = os.environ.get("COACH_WEBHOOK_SECRET")
    header = request.headers.get("X-Auth", "")
    if not secret or header != secret:
        return jsonify(error="unauthorized"), 401

    # Basic payload validation
    data = request.get_json(silent=True) or {}
    event = data.get("event", "morning")
    context = data.get("context", "")
    length = data.get("len", "short")

    # Placeholder response (replace with OpenAI call in production)
    response = {
        "event": event,
        "context": context,
        "length": length,
        "coach_message": "Good morning — try a 2-minute breathing exercise and set one small intention for today."
    }

    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, jsonify
import os
app = Flask(__name__)
@app.get("/status")
def status():
    return jsonify(ok=True)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
from flask import Flask, request, jsonify
from datetime import datetime
import os
from openai_service import OpenAIService
from memory import MemoryStore

app = Flask(__name__)

# Initialize services
openai_service = OpenAIService(api_key=os.getenv('OPENAI_API_KEY'))
memory_store = MemoryStore()

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'service': 'Morning Coach API',
        'version': '3.0',
        'status': 'running',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/coach', methods=['POST'])
def coach():
    """Main coaching endpoint"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        user_id = data.get('user_id', 'anonymous')
        message = data.get('message', '')
        context = data.get('context', {})

        if not message:
            return jsonify({'error': 'Message is required'}), 400

        # Get user history
        history = memory_store.get_history(user_id)

        # Generate coaching response
        response = openai_service.generate_coaching_response(
            message=message,
            context=context,
            history=history
        )

        # Store interaction
        memory_store.add_interaction(user_id, message, response)

        return jsonify({
            'user_id': user_id,
            'response': response,
            'timestamp': datetime.utcnow().isoformat()
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history/<user_id>', methods=['GET'])
def get_history(user_id):
    """Get user conversation history"""
    history = memory_store.get_history(user_id)
    return jsonify({
        'user_id': user_id,
        'history': history,
        'count': len(history)
    })

@app.route('/api/history/<user_id>', methods=['DELETE'])
def clear_history(user_id):
    """Clear user conversation history"""
    memory_store.clear_history(user_id)
    return jsonify({
        'user_id': user_id,
        'status': 'cleared'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

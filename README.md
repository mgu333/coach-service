# Morning Coach Service v3

A Flask-based REST API for an AI-powered morning coaching service using OpenAI's GPT models.

## Features

- 🌅 Personalized morning coaching conversations
- 💬 Conversation history tracking per user
- 🧠 Context-aware responses using GPT-4
- 🚀 Ready for deployment on Railway, Heroku, or Docker
- 📊 Simple REST API interface

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

3. Run the service:
```bash
python app.py
```

### Deployment Options

#### Railway
1. Create new project on Railway
2. Add environment variable: `OPENAI_API_KEY`
3. Deploy from GitHub or upload files
4. Railway will auto-detect and use Dockerfile

#### Heroku
```bash
heroku create your-app-name
heroku config:set OPENAI_API_KEY='your-api-key-here'
git push heroku main
```

#### Docker
```bash
docker build -t morning-coach .
docker run -p 5000:5000 -e OPENAI_API_KEY='your-key' morning-coach
```

## API Endpoints

### POST /api/coach
Send a message to the morning coach.

**Request:**
```json
{
  "user_id": "user123",
  "message": "I'm feeling unmotivated this morning",
  "context": {
    "time_zone": "PST",
    "mood": "low"
  }
}
```

**Response:**
```json
{
  "user_id": "user123",
  "response": "I hear you - mornings can be tough! What's one small thing that usually makes you feel better?",
  "timestamp": "2025-01-15T08:30:00"
}
```

### GET /api/history/{user_id}
Retrieve conversation history for a user.

### DELETE /api/history/{user_id}
Clear conversation history for a user.

### GET /
Health check endpoint.

## Environment Variables

- `OPENAI_API_KEY` (required): Your OpenAI API key
- `PORT` (optional): Server port, defaults to 5000

## Testing

Run the test suite:
```bash
python test_service.py
```

Or use the CURL examples:
```bash
bash CURL_EXAMPLES.sh
```

## Architecture

- **app.py**: Main Flask application with API routes
- **openai_service.py**: OpenAI integration and prompt management
- **memory.py**: In-memory conversation storage
- **Dockerfile**: Container configuration
- **Procfile**: Process configuration for Platform-as-a-Service

## License

MIT License - Feel free to use and modify!

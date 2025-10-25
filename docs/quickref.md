# Quick Reference - Coach Service

## Deploy Commands (Railway)

### Install Railway CLI
```bash
npm i -g @railway/cli
# or
brew install railway
```

### Login and Link Project
```bash
railway login
railway link
```

### Deploy to Railway
```bash
# Deploy current branch
railway up

# Deploy with specific environment
railway up --environment production

# Deploy and follow logs
railway up && railway logs
```

### Check Deployment Status
```bash
# View current deployment
railway status

# View logs
railway logs

# Follow logs in real-time
railway logs -f
```

## Local Development Commands

### Setup Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Flask Application
```bash
# Development mode
flask run

# With specific host and port
flask run --host=0.0.0.0 --port=5000

# Debug mode
FLASK_ENV=development flask run

# Using Python directly
python app.py
```

## Testing Commands

### Run Tests
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_service.py

# Run with coverage
pytest --cov=. --cov-report=html
```

### Manual API Testing
```bash
# Test local endpoint
curl http://localhost:5000/health

# Test Railway deployment
curl https://your-app.railway.app/health

# Use CURL_EXAMPLES.sh for more examples
bash CURL_EXAMPLES.sh
```

## Troubleshooting Commands

### Railway Diagnostics
```bash
# Check environment variables
railway variables

# Open Railway dashboard
railway open

# Check service status
railway status

# View recent logs with errors
railway logs | grep -i error
```

### Docker Commands (Local Testing)
```bash
# Build Docker image
docker build -t coach-service .

# Run container locally
docker run -p 5000:5000 coach-service

# Run with environment variables
docker run -p 5000:5000 --env-file .env coach-service

# Check container logs
docker logs <container_id>

# Interactive shell in container
docker exec -it <container_id> /bin/bash
```

### Python/Flask Debugging
```bash
# Check Python version
python --version

# Verify dependencies
pip list

# Check for dependency issues
pip check

# Update requirements
pip freeze > requirements.txt

# Test imports
python -c "import flask; import openai; print('OK')"
```

### Network/API Debugging
```bash
# Test endpoint with verbose output
curl -v http://localhost:5000/health

# Check response headers
curl -I http://localhost:5000/health

# Test POST endpoint
curl -X POST http://localhost:5000/api/endpoint \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
```

### Common Issues & Fixes

#### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill process
kill -9 <PID>
```

#### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Clear pip cache
pip cache purge
```

#### Railway Environment Variables
```bash
# Set variable
railway variables set KEY=value

# List all variables
railway variables list

# Delete variable
railway variables delete KEY
```

## Git Workflow

```bash
# Check status
git status

# Create feature branch
git checkout -b feature/my-feature

# Stage and commit changes
git add .
git commit -m "feat: description"

# Push to remote
git push origin feature/my-feature

# Update main branch
git checkout main
git pull origin main
```

## Useful Links

- Railway Dashboard: https://railway.app/dashboard
- Flask Documentation: https://flask.palletsprojects.com/
- OpenAI API Docs: https://platform.openai.com/docs/api-reference

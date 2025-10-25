FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 5000

# Run with gunicorn
CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 60

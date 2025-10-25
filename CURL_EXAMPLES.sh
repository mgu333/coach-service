#!/bin/bash

# Morning Coach Service - CURL Examples
# Update BASE_URL to your deployed service URL

BASE_URL="http://localhost:5000"

echo "==================================="
echo "Morning Coach Service - CURL Tests"
echo "==================================="

# 1. Health Check
echo -e "\n1. Health Check"
curl -X GET "$BASE_URL/" | jq .

# 2. Send a coaching message
echo -e "\n2. Send Coaching Message"
curl -X POST "$BASE_URL/api/coach" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "demo_user",
    "message": "I want to be more productive today but I feel overwhelmed",
    "context": {
      "time": "8:00 AM",
      "mood": "anxious"
    }
  }' | jq .

# 3. Another message from the same user
echo -e "\n3. Follow-up Message"
curl -X POST "$BASE_URL/api/coach" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "demo_user",
    "message": "Thanks! What should I tackle first?"
  }' | jq .

# 4. Get conversation history
echo -e "\n4. Get Conversation History"
curl -X GET "$BASE_URL/api/history/demo_user" | jq .

# 5. Clear conversation history
echo -e "\n5. Clear Conversation History"
curl -X DELETE "$BASE_URL/api/history/demo_user" | jq .

# 6. Verify history is cleared
echo -e "\n6. Verify History Cleared"
curl -X GET "$BASE_URL/api/history/demo_user" | jq .

echo -e "\n==================================="
echo "Tests Complete!"
echo "==================================="

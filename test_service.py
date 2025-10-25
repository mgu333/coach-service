import requests
import json

# Change this to your deployed URL or keep as localhost for local testing
BASE_URL = "http://localhost:5000"

def test_health():
    """Test the health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def test_coaching():
    """Test the main coaching endpoint"""
    print("\n=== Testing Coaching Endpoint ===")

    payload = {
        "user_id": "test_user_123",
        "message": "I'm feeling really tired this morning and don't want to get out of bed.",
        "context": {
            "time": "7:00 AM",
            "mood": "low"
        }
    }

    response = requests.post(
        f"{BASE_URL}/api/coach",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def test_history():
    """Test retrieving conversation history"""
    print("\n=== Testing History Retrieval ===")

    user_id = "test_user_123"
    response = requests.get(f"{BASE_URL}/api/history/{user_id}")

    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

def test_clear_history():
    """Test clearing conversation history"""
    print("\n=== Testing History Clearing ===")

    user_id = "test_user_123"
    response = requests.delete(f"{BASE_URL}/api/history/{user_id}")

    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    return response.status_code == 200

if __name__ == "__main__":
    print("Morning Coach Service - Test Suite")
    print("=" * 50)

    tests = [
        ("Health Check", test_health),
        ("Coaching", test_coaching),
        ("History Retrieval", test_history),
        ("Clear History", test_clear_history)
    ]

    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, "PASS" if result else "FAIL"))
        except Exception as e:
            print(f"Error in {test_name}: {str(e)}")
            results.append((test_name, "ERROR"))

    print("\n" + "=" * 50)
    print("Test Results:")
    for test_name, status in results:
        print(f"  {test_name}: {status}")

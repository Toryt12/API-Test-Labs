import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def test_get_post(post_id=1):
    response = requests.get(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "title" in data, "Missing 'title' in response"
    print(f"✅ GET /posts/{post_id} passed")

def test_create_post():
    payload = {"title": "QA Lab", "body": "Testing API", "userId": 1}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    print("✅ POST /posts passed")

if __name__ == "__main__":
    test_get_post()
    test_create_post()

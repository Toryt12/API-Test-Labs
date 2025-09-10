# 🧪 Test Case: GET /posts/{id}

**Objective**: Validate that the API returns correct post data for a given ID

**Endpoint**: `GET https://jsonplaceholder.typicode.com/posts/{id}`  
**Method**: GET  
**Test Data**: `id = 1`

## ✅ Expected Results
- Status code: `200 OK`
- Response contains keys: `userId`, `id`, `title`, `body`
- `title` is a non-empty string

## 🐛 Edge Cases
- `id = 0` → Expect `404 Not Found`
- `id = abc` → Expect `400 Bad Request` or graceful failure

## 🔍 Validation Steps
1. Send GET request with valid ID
2. Assert status code
3. Parse JSON and validate keys

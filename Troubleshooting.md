# 🐛 Troubleshooting Log: API Test Automation Lab

---

## ❌ Error: `ConnectionError`
**Context**: API unreachable during GET request  
**Root Cause**: Incorrect base URL or network issue  
**Resolution**: Verified endpoint and retried with correct URL  
**Lesson**: Always validate base URL and test connectivity before scripting

---

## ❌ Error: `JSONDecodeError`
**Context**: Response parsing failed  
**Root Cause**: Response was HTML or empty, not JSON  
**Resolution**: Added `response.headers` check and fallback logic  
**Lesson**: Never assume response format—validate before parsing

---

## ❌ Error: `401 Unauthorized`
**Context**: POST request failed due to missing auth  
**Root Cause**: API key not included in headers  
**Resolution**: Added `Authorization` header with token  
**Lesson**: Secure endpoints require proper headers—always check docs

---

## ✅ Enhancements
- Added assertions for status codes and payload keys
- Modularized test functions for reuse
- Documented lessons learned for future labs

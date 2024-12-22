# 📑 Security and Authentication

APIs enable third-party applications to interact with servers and databases, making robust security practices essential. Below are key security concepts to protect your API.

## 1. **SSL (Secure Socket Layer)**

- **What:** Encrypts data transmitted between the client and server.
- **Why:** Prevents attackers from intercepting sensitive information.
- **How:** Use HTTPS instead of HTTP by obtaining an SSL/TLS certificate.

**Example:**

```
https://api.example.com/users
```

---

## 2. **Signed URLs**

- **What:** Generate URLs with a signature to ensure they are valid and unaltered.
- **Why:** Prevent unauthorized access to resources, especially for file downloads or temporary access.
- **How:** Append a signature and expiry timestamp to the URL.

**Example:**

```
https://api.example.com/resource?signature=abc123&expires=1700000000
```

---

## 3. **Authentication**

- **What:** Verifies the identity of API users.
- **Why:** Ensures only authorized users can access the API.
- **How:** Implement authentication methods like API keys, OAuth, or JWT (JSON Web Tokens).

**Example:**

- API Key in Header:

```
GET /resource
Header: Authorization: Bearer api_key_123
```

- JWT:

```
Header: Authorization: Bearer eyJhbGciOiJIUzI1...
```

---

## 4. **CORS (Cross-Origin Resource Sharing)**

- **What:** Controls which domains can access your API.
- **Why:** Prevents malicious websites from making unauthorized API requests.
- **How:** Configure your API to allow specific origins in the server settings.

**Example:** CORS Header:

```
Access-Control-Allow-Origin: https://trusted-domain.com
```


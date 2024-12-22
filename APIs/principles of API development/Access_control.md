# 📑 Access Control (Authorization)

### Key Concepts
- **Authentication:** Let you get in the website.
- **Authorization:** what you can do once you are in.

## 📑 **Token-Based Authorization**

- **What:** Use tokens like JWT (JSON Web Tokens) to manage access.
- **Why:** Stateless and secure, making it ideal for distributed systems.

**Example:**
JWT Payload:
```
{
  "sub": "1234567890",
  "role": "admin",
  "exp": 1700000000
}
```
Verify role and expiration before granting access.
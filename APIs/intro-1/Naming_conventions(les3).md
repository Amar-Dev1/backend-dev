# 📑 Naming Conventions for RESTful APIs

To ensure best practices and maintain readability, consistency, and usability in RESTful APIs, you should follow these guidelines:

---

## 1. Use Lowercase Letters
- **Why?**  
  Consistent and readable URLs avoid issues with case sensitivity across different platforms.
- **Example:**  
```url
✅ GET /users
❌ GET /Users
```
## 2. Use Forward Slashes (`/`) to Indicate Hierarchy
- **Why?**  
Forward slashes clearly define resource relationships and hierarchy in the URL structure.
- **Example:**  
```url
✅ GET /users/123/orders
❌ GET /users:123:orders
```
## 3. Use Nouns for Collections, Not Verbs
- **Why?**  
RESTful APIs represent resources (nouns), not actions (verbs). HTTP methods already specify the action.
- **Example:**  
```url
✅ GET /users
❌ GET /getUsers
```
## 4. Avoid File Name Extensions
- **Why?**  
APIs should return content based on headers (`Accept` or `Content-Type`) rather than embedding file types in the URL. This ensures flexibility.
- **Example:**  
```url
✅ GET /reports
❌ GET /reports.json
```
## 5. Use Query Parameters for Filtering, Sorting, and Pagination
- **Why?**  
Query parameters help refine the data requested, keeping the endpoints clean and reusable.
- **Example:**  
```url
✅ GET /products?category=electronics&sort=price&page=2
❌ GET /products/electronics/sort/price/page/2
```
## 6. No Trailing Slash
- **Why?**  
Trailing slashes can create inconsistencies or duplicate routes in some systems.
- **Example:**  
```url
✅ GET /users
❌ GET /users/
```





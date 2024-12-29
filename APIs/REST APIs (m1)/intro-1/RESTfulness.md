# 📘 RESTfulness

## 📑 What is REST?
REST (Representational State Transfer) is an architectural style used to design APIs. It provides a structured approach to enable seamless communication between clients and servers for accessing and manipulating data.

Key characteristics of REST:
- Simplicity and ease of communication between client and server.
- Resource-based interactions using standard HTTP methods.
- Built on six core principles.

---

## 📑 Principles of RESTful APIs

To qualify as a RESTful API, the following principles must be adhered to:

1. **Client-Server Architecture**  
   - Separation of concerns between the client and server.
   - Clients handle user interfaces and user experiences, while servers manage data and logic.

2. **Stateless**  
   - Each request from a client contains all the information needed for the server to process it.
   - The server does not store any session information about the client between requests.

3. **Cacheable**  
   - Responses can be cached by the client to improve performance and reduce server load.
   - Server responses must define whether caching is permitted or not.

4. **Uniform Interface**  
   - Consistent interface for communication between the client and server.
   - Typically follows standards like HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) and uses URIs for resource identification.

5. **Layered System**  
   - A RESTful system can consist of multiple layers, where each layer has specific responsibilities.  
   - This helps improve scalability, flexibility, and security. (See table below for details.)

6. **Code on Demand** *(Optional)*  
   - Servers can extend client functionality by sending executable code, such as JavaScript, to be executed on the client side.

---

# 📑 RESTful API System

| Component         | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| **Client**         | Sends requests to access or manipulate resources.                         |
| **Firewall**       | Protects the server by filtering unauthorized or harmful requests.         |
| **Load Balancer**  | Distributes incoming requests across multiple servers to ensure stability. |
| **Web Server**     | Handles HTTP requests and serves content or processes API logic.           |
| **Database Server**| Stores and manages the application's data persistently.                    |

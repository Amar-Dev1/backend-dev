# 📑 JWT in DRF

JWT (JSON Web Token) is a compact, URL-safe token format used to securely transmit information between parties. It is commonly used for authentication in web applications .

## 💡 How JWT Works
1. **User Logs In**: The user sends their credentials (username and password) to the server.
2. **Token Issued**: The server verifies the credentials and generates a JWT.
3. **Client Stores Token**: The client stores the token (usually in localStorage or sessionStorage).
4. **Token Used for Requests**: The client sends the JWT with each request to access protected resources.
5. **Server Verifies Token**: The server validates the token and processes the request.

## Setting Up JWT in DRF

### 1. Install Required Packages
Install the `djangorestframework-simplejwt` package:
```bash
pip install djangorestframework-simplejwt
```

### 2. Update `settings.py`
Add JWT authentication to the `DEFAULT_AUTHENTICATION_CLASSES`:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```

### 3. Configure JWT Settings (Optional)
You can customize JWT settings in `settings.py`:
```python
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
```

### 4. Add JWT Endpoints
Include JWT views in your `urls.py`:
```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...,
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 5. Using JWT in Requests
#### Obtain a Token
Make a `POST` request to `/api/token/` with the user credentials:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
Response:
```json
{
    "access": "<ACCESS_TOKEN>",
    "refresh": "<REFRESH_TOKEN>"
}
```

#### Access Protected Resources
Send the `access` token in the `Authorization` header:
```
Authorization: Bearer <ACCESS_TOKEN>
```

#### Refresh Token
To get a new access token, make a `POST` request to `/api/token/refresh/` with the `refresh` token:
```json
{
    "refresh": "<REFRESH_TOKEN>"
}
```
Response:
```json
{
    "access": "<NEW_ACCESS_TOKEN>"
}
```

## Notes
- JWT is stateless, meaning the server does not store session data.
- Use HTTPS to secure communication between the client and server.
- Keep the `refresh` token safe, as it can be used to generate new access tokens.

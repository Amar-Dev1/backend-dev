# 📑 Token-Based Authentication in DRF

Token-Based Authentication allows clients to authenticate and access protected endpoints by using a unique token provided by the server.

## 💡 Overview
1. The client sends their **username** and **password** to the server.
2. If the credentials are valid, the server generates a unique token for the user.
3. The client includes the token in the `Authorization` header for subsequent requests.
4. The server validates the token to identify the user and authorize access to protected resources.

---

## ⚡ Implementation Steps

### 1. Enable Token Authentication
Add `'rest_framework.authtoken'` to the `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',
]
```
Run migrations to create the necessary database tables:
```bash
python manage.py migrate
```

### 2. Generate a Token for a User
You can generate tokens for users via the Django admin panel or programmatically:
```python
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username="your_username")
token, created = Token.objects.get_or_create(user=user)
print(token.key)  # Print the generated token
```

### 3. Create a Protected API Endpoint
Define a protected endpoint that requires authentication:
```python
# views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "This is a secret message."})
```
Add the endpoint to your `urls.py`:
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('secret/', views.secret, name='secret'),
]
```

### 4. Configure DRF for Token-Based Authentication
In `settings.py`, configure the `DEFAULT_AUTHENTICATION_CLASSES`:
```python
REST_FRAMEWORK = {
    ...,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
}
```

### 5. Generate Token via API Endpoint
Use DRF's built-in `obtain_auth_token` view to allow users to generate tokens:
```python
# urls.py
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
```
This endpoint accepts a `POST` request with `username` and `password`:
#### Request Example:
```json
{
    "username": "your_username",
    "password": "your_password"
}
```
#### Response Example:
```json
{
    "token": "your_generated_token"
}
```

### 6. Use Token in Requests
Include the token in the `Authorization` header for all protected endpoints:
```
Authorization: Token your_generated_token
```

---

## Summary of Endpoints
- **Token Generation**: `/api-token-auth/`
- **Protected Endpoint**: `/secret/`

### Notes
- Tokens can be generated once and reused unless explicitly revoked.
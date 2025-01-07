# 📑 Token-Based Authentication

## 💡 Overview
1. Users send their **username** and **password** once.
2. If credentials are valid, the server generates a unique token.
3. The server decides the token's validity duration and expiration time.
4. For subsequent requests, the client includes the token in the request header.
5. The server validates the token using the DRF `Authentication` class and identifies the associated user.

---

## 📑 Implementation Steps
### 1. Enable Token Authentication
In `settings.py`, include `'rest_framework.authtoken'` in `INSTALLED_APPS`.
- ❗ then make `migrations`
### 2. Generate a Token
Generate a token for a user via the Django admin panel.

### 3. Create a Protected API Endpoint with its url
```python
#views.py

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response("This is a secret message.")

# urls.py
path("secret", views.Secrect),
```
### 4. Configure DRF for Token-Based Authentication
In `settings.py`, add the following:
```python
REST_FRAMEWORK = {
    ...,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

```
### 💡 Note
the Token in request header be like : `Authorization: Token alskadj32flkj20kdsjflhgf9493489203`

## 📑 Generate Token via API Endpoint
Use the `obtain_auth_token` class from `rest_framework.authtoken.views`:
```python
# urls.py
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
]
```
- This endpoint accepts HTTP `POST` requests with `username` and `password` as parameters.
- The response will include a token, which can be used for accessing protected URLs.

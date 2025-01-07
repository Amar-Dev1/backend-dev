# Djoser

Djoser is a library designed to simplify authentication and authorization in Django REST Framework projects.

## How to Use Djoser

### 1. Install Djoser
Activate your virtual environment and run:
```bash
pipenv install djoser
```

### 2. Add Djoser to `INSTALLED_APPS`
In your `settings.py`, include `djoser` after `rest_framework`:
```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'djoser',
]
```

### 3. Configure Djoser Settings
Create a `DJOSER` section in `settings.py` to specify the primary key field for users:
```python
DJOSER = {
    'USER_ID_FIELD': 'username',  # Use "username" as the primary key
}
```

### 4. Add Authentication Classes
Ensure you add the authentication classes in the `REST_FRAMEWORK` settings:
```python
REST_FRAMEWORK = {
    ...,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # For admin interface
        'rest_framework.authentication.TokenAuthentication',
    ),
}
```

### 5. Enable Djoser Endpoints
Add the following paths in your project-level `urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    ...,
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
```

## Djoser Endpoints
Some useful endpoints provided by Djoser:

- `/auth/users/` - User list and creation
- `/auth/users/me/` - Current user details
- `/auth/users/login/` - Login user

### Notes
- Add authentication classes in `REST_FRAMEWORK` to enable Djoser functionality.
- Use tools like **Insomnia**, **Postman**, or the **Browsable API** to test Djoser endpoints.

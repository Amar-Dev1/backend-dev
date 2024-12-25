# 📑Routing in DRF

## Introduction
- 💡DRF provides several ways to handle URL mapping (routing) in the API projects. Here guide explains the key techniques, from basic to advanced :
---

## 1. **Regular Routes**
This is the traditional way of mapping URLs to function-based views.

### Example:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),  # Maps the function to /api/books
]
```
- You can specify allowed HTTP methods using DRF's `@api_view` decorator in the `views.py` file.

---

## 2. **Routing to Class Methods**
If you map specific methods of a class, declare those methods as `@staticmethod` first.

### Example:
**views.py**:
```python
class Orders:
    @staticmethod
    def listOrders(request):
        # Logic here
        pass
```
**urls.py**:
```python
urlpatterns = [
    path('orders', views.Orders.listOrders),
]
```

---

## 3. **Routing Class-Based Views**
Use class-based views that extend `APIView`. This avoids mapping each method individually.

### Example:
**views.py**:
```python
from rest_framework.views import APIView

class Books(APIView):
    def get(self, request, bookId):
        # GET logic
        pass

    def put(self, request, bookId):
        # PUT logic
        pass
```
**urls.py**:
```python
urlpatterns = [
    path('books/<int:bookId>', views.Books.as_view()),
]
```
- Methods like `post()`, `delete()`, and `patch()` can also be added for other HTTP methods.

---

## 4. **Routing Classes That Extend ViewSets**
ViewSets simplify routing by grouping related actions.

### Example:
**views.py**:
```python
from rest_framework import viewsets

class BooksViewSet(viewsets.ViewSet):
    def list(self, request):
        # Logic for listing all books
        pass

    def retrieve(self, request, pk=None):
        # Logic for retrieving a single book
        pass
```
**urls.py**:
```python
from rest_framework.routers import SimpleRouter
from .views import BooksViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'books', BooksViewSet, basename='book')

urlpatterns = router.urls
```
- Access `/api/books` (GET, POST) and `/api/books/1` (GET, PUT, PATCH, DELETE).

---

## 5. **Routing with `SimpleRouter`**
`SimpleRouter` simplifies routing for `ViewSet` classes.

### Example:
```python
from rest_framework.routers import SimpleRouter
from .views import BooksViewSet

router = SimpleRouter(trailing_slash=False)  # Avoids trailing slashes
router.register(r'books', BooksViewSet, basename='book')

urlpatterns = router.urls
```

---

## 6. **Routing with `DefaultRouter`**
`DefaultRouter` provides an API root endpoint listing all available endpoints.

### Example:
```python
from rest_framework.routers import DefaultRouter
from .views import BooksViewSet

router = DefaultRouter()  # Includes a root view
router.register(r'books', BooksViewSet, basename='book')

urlpatterns = router.urls
```
- Access `/api/books`, `/api/books/1`, and `/api/` (root view displaying all endpoints).

---

## Key Notes:
- **Regular routes**: Simple and manual.
- **Class-based views**: Avoid repetitive mappings; ideal for specific logic.
- **ViewSets with routers**: Best for consistent, CRUD-based APIs.
- Use `SimpleRouter` for clean URLs and `DefaultRouter` for a root endpoint overview.

---

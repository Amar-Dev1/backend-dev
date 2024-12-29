# Generic Views and ViewSets in DRF

## Introduction
Django Rest Framework (DRF) includes generic views and ViewSets to streamline API development. These tools reduce the amount of code needed to build a fully functional API. This guide introduces the different types of generic views and ViewSets, their purposes, and benefits.

---

## ViewSets

### Overview
ViewSets are simplified class-based views that come with additional features, such as:
- Automatic routing
- Browsable API views
- Integration with permission and throttle classes

To use ViewSets, import the `viewsets` module from `rest_framework`:
```python
from rest_framework import viewsets
```

### Types of ViewSets

#### 1. **ViewSet**
- Extends `APIView`.
- Provides a method-naming convention for routing.
- Handles collections of resources with:
  - `list()`: Handles `GET` requests to display resource collections.
  - `create()`: Handles `POST` requests to create new resources.
- Handles single resources with:
  - `retrieve()`: Handles `GET` requests to display a single resource.
  - `update()`: Handles `PUT` requests to completely replace a resource.
  - `partial_update()`: Handles `PATCH` requests to partially update a resource.
  - `destroy()`: Handles `DELETE` requests to delete a resource.

Example:
```python
class MyViewSet(viewsets.ViewSet):
    def list(self, request):
        pass  # Logic for listing resources

    def retrieve(self, request, pk=None):
        pass  # Logic for retrieving a single resource
```

#### 2. **ModelViewSet**
- Automatically handles CRUD operations.
- Requires only a `queryset` and a `serializer`.

Example:
```python
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

#### 3. **ReadOnlyModelViewSet**
- Handles only `GET` requests (no write operations).
- Useful for read-only APIs.

Example:
```python
class MyReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

---

## Generic Views

### Overview
Generic views simplify API development by automating common patterns. To use them, import the `generics` module from `rest_framework`:
```python
from rest_framework import generics
```

### Common Generic Views

| Generic View Class           | Supported Methods         | Purpose                                         |
|------------------------------|---------------------------|------------------------------------------------|
| `CreateAPIView`              | `POST`                   | Create a new resource                          |
| `ListAPIView`                | `GET`                    | Display a collection of resources              |
| `RetrieveAPIView`            | `GET`                    | Display a single resource                      |
| `DestroyAPIView`             | `DELETE`                 | Delete a single resource                       |
| `UpdateAPIView`              | `PUT`, `PATCH`           | Update or partially update a resource          |
| `ListCreateAPIView`          | `GET`, `POST`            | List resources and create a new resource       |
| `RetrieveUpdateAPIView`      | `GET`, `PUT`, `PATCH`    | Retrieve and update a resource                 |
| `RetrieveDestroyAPIView`     | `GET`, `DELETE`          | Retrieve and delete a resource                 |
| `RetrieveUpdateDestroyAPIView`| `GET`, `PUT`, `PATCH`, `DELETE` | Full CRUD operations on a single resource |

### Example
- Using `ListCreateAPIView` to handle both listing and creating resources:

```python
class MyListCreateView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
```

---

## Authentication and Selective Authentication

### Authentication for All API Calls
Add `permission_classes` to enforce authentication for all calls:
```python
from rest_framework.permissions import IsAuthenticated

class MyView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = [IsAuthenticated]
```

### Selective Authentication
Override the `get_permissions` method to enable authentication only for specific methods:
```python
class MyView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return []
```

---

## Customizing Querysets
To return resources created by the authenticated user only, override the `get_queryset` method:
```python
class MyView(generics.ListAPIView):
    serializer_class = MyModelSerializer

    def get_queryset(self):
        return MyModel.objects.filter(user=self.request.user)
```

---

## Overriding Default Behavior
You can override any method to change default behavior. Example:
```python
class MyCustomView(generics.ListAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def list(self, request, *args, **kwargs):
        return Response({"message": "Custom response"})
```

---

# 📑Ordering & Pagination in ( class-based views )

- 💡 we can use `viewsets` to quick implement CRUD API endpoints

## ❗ After installing `django-filter`
### 📑Step 1 : `views.py`
```python
from rest_framework.response import Response
from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer  
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
```
### 📑Step 2 : `urls.py`
```python
from django.urls import path 
from . import views 
urlpatterns = [ 
    path('menu-items',views.MenuItemsViewSet.as_view({'get':'list'})),
    path('menu-items/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
]
```
### 📑Step 3 : `settings.py`
```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        ...
    ],
    ## add this section 👇
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
}
```

## 1️⃣ Ordering and sorting
- To implement sorting by the price,stock fields you can use DRF’s built-in ordering classes
- You can do this by specifying these two fields in the `ordering_fields` list in the `MenuItemsViewSet` class.
```python
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price','stock']
```

## 2️⃣ Pagination
- Using DRF’s built-in pagination classes makes paginating the API result very easy
- Add these two lines in the `REST_FRAMEWORK` section in the `settings.py`
```python
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
'PAGE_SIZE': 2
```
- 💡`PAGE_SIZE` property tells DRF how many items to show per page

## 3️⃣ Search
- add `search_fields=['title']` in the `MenuItemsViewSet` class.
```python 
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price','stock']
    search_fields=['title']
```
- **💡The default `lookup_field` value for searching in DRF is `icontains`, for example :**
#### If the client searches for ILLA it will match every menu item where the title has ILLA in a case-insensitive fashion

----------

- **💡to do nested search (like search into category title)**
```python
search_fields=['title','category__title']
```
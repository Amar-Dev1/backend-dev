# 📑 CRUD operations using `Generics`

## 📑 Resturant menu items example : 
```python 
# views.py

from rest_framework import generics
from .model import MenuItems
from .serializers import MenuItemsSerializer

# to handle with menu items operations : (GET,POST )
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

# to handle wiht item operations (full CRUD)
class singleMenuItemView(generics.RetriveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer

# urls.py

from django.urls import path
from . import views

urlpattern = [
    path('menuitems/', views.MenuItemsView.as_view()),
    path('menuitems/<int:pk>/', views.singleMenuItemView.as_view()),
]
```
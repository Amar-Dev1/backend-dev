# 📑 Serializers in Django Rest Framework (DRF)

## What are Serializers?
Serializers are used to convert complex data types (e.g., Django model instances or Python objects) into formats like **JSON** or **XML**, making them suitable for rendering as API responses.

## What are Deserializers?
Deserializers perform the opposite operation of serializers: they convert data from formats like **JSON** or **XML** into Python objects. This is useful for validating and processing input data from the client.

## 💡 Key Notes
- Serializers and deserializers are tools for converting data between different formats.
- Use **deserializers** to validate and convert client data (e.g., `JSON/XML` to `Python objects`).
- Use **serializers** to send data to the client (e.g., Python `objects/models` to `JSON/XML`).

---

## Examples of Serializers

### Simple Serializer Example
```python
# serializers.py

from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()

    # the output will display only title and price field

# views.py
from rest_framework.decorators import api_view
from .serializers import MenuItemSerializer
from .models import MenuItem

@api_view
def menu_item(request):
    items= MenuItem.objects.all()
    serialized_item = MenuItemSerializer(item,many=True)
    return Response(serialized_item.data)

    # many=True => is essential when converting a list into JSON data    
```
## 💡Note
- its not required to convert a single object (single item) to `JSON`

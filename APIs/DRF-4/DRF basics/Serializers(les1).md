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
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
```

### Model Serializer Example
```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price']

# This serializer integrates with the Book model ✅

# 🖑 Deserialization & Validation

## 💡 Deserialization
Deserialization is the process of converting data received from the client (often in JSON format) back into Python objects. It also includes **validating** the data to ensure it adheres to the required structure and rules.

## 💡 Validation
Validation is the process of checking whether the deserialized data is correct and meets the expected format, constraints, and rules.

---

## ✅ Steps to Validate Data Using Deserialization

### 1️⃣ Pass the Request to a Serializer  
The serializer takes the incoming data (e.g., JSON) and converts it into Python objects.  

```python
from .serializers import MenuItemSerializer

serialized_item = MenuItemSerializer(items, many=True)

return Response(serialized_item.data)
```

### 2️⃣ Validate the Serialized Data
- Use the `is_valid()` method of the serializer to validate the data:

```python
from .serializers import MenuItemSerializer

serializer = MenuItemSerializer(data=request.data)  # Pass the client-provided data
if serializer.is_valid(raise_exception=True):  
    # Perform additional logic here (e.g., saving the validated data)
    serializer.save()
    return Response({"message": "Data saved successfully!"})

return Response(serializer.errors, status=400)
```

---

## 🖋️ `read_only` and `write_only` Properties in Deserialization

When working with Django REST Framework (DRF) serializers, you can use the `read_only` and `write_only` attributes to control how fields are handled during serialization and deserialization.

---

### 💡 What is `read_only`?  
Fields marked as `read_only` are included in the serialized output but **cannot** be used in the deserialization process (e.g., when creating or updating data).

### Example:
Imagine a scenario where an `id` field should only be included in the **response**, not in the **request**.

```python
from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # This field is read-only
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
```

#### Usage:
- **Serialization (Output):**
```json
{
    "id": 1,
    "name": "Pizza",
    "price": 10.99
}
```
- **Deserialization (Input):**
```json
{
    "name": "Burger",
    "price": 8.99
}
```

---

### 💡 What is `write_only`?  
Fields marked as `write_only` are used during deserialization (e.g., input data from a request) but not included in the serialized output.

### Example:
Imagine a password field that should only be used when creating or updating an object, not when retrieving it.

```python
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)  # This field is write-only
```

#### Usage:
- **Serialization (Output):**
```json
{
    "username": "john_doe"
}
```
- **Deserialization (Input):**
```json
{
    "username": "john_doe",
    "password": "secure_password"
}
```

---

## 🛠️ Combined Example: Using `read_only` and `write_only` Together

```python
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # Automatically generated, not user-input
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    secret_code = serializers.CharField(write_only=True)  # Used for special operations, hidden in responses
```

### Usage:
- **Input (Deserialization):**
```json
{
    "name": "Laptop",
    "price": 999.99,
    "secret_code": "special123"
}
```

- **Output (Serialization):**
```json
{
    "id": 42,
    "name": "Laptop",
    "price": 999.99
}
```


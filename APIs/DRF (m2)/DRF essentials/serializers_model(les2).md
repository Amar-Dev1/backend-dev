# 📑Serializers model
- 💡this serializer integrate with model

## Example
```python 
from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.SerializerModel):
    class Meta:
        model = MenuItem
        fields = ['id','title','price']
```

## 🖋 Change field`s name 
- 💡we can change the field`s name in the serializer by using the `source` parameter
```python
from rest_framework import serializers
from .models import MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    head = serializer.CharField(source=title)
    class Meta:
        model = MenuItem
        fields = ['id','head','price']

```

## 📝 proccess field
- 🧮calculate the price_after_tax
```python 
from rest_framework import serializers
from .models import MenuItem
class MenuItemSerializer(serializers.ModelSerializer):
    head = serializer.CharField(source=title)
    price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    class Meta:
        model = MenuItem
        fields = ['id','head','price']
def calculate_tax(self, product:MenuItem):
    return product.price * 1.08
```
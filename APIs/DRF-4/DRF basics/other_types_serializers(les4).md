# 📑DRF Serialization Techniques

## 📑Overview
This guide covers techniques for serializing model relationships in **DRF**. It includes:
1. Nested fields with `depth` or custom serializers.
2. Displaying related fields as hyperlinks with `HyperlinkedRelatedField` and `HyperlinkedModelSerializer`.

---

## 1. Nested Fields

### Method 1: Using a Custom Serializer
- Create a serializer for the related model and include it in the main serializer.
like what we created a separete serializer for **category**.
### Method 2: Using `depth

- Set `depth = 1`in the serializer Meta class to display nested fields **automatically**.
```python 

class MenuItemSerializer(serializers.ModelSerializer):
   ...

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']
        depth = 1

    ...
```


## 2. Hyperlinked Fields 

### Method 1: Using `HyperlinkedRelatedField`
1. define a view function :
```python
@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)
```
2. Map the View in `urls.py` :
```python 
urlpatterns = [
   🖋 path('category/<int:pk>', views.category_detail, name='category-detail'),
]
```
3. Update the Serializer :
```python 
from .models import Category

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    🖋 category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='category-detail'
    )

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)

```
4. Add Context :
```python 
🖋 serialized_item = MenuItemSerializer(items, many=True, context={'request': request})

```

### Method 2: Using `HyperlinkedModelSerializer` : 
- use it for cleaner code 
```python 
class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category']

    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)

```
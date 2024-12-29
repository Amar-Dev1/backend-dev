# 📑Relationship serializers

## 🖋 Example
```python

# models.py
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()

class MenuItem(models.Model):
    title = models.Charfield()
    price = models.DeciamlField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# serializers.py
...

class CategorySerializer(...):
    class Meta:
        ...
        fields = ['id','slug','title']

class MenuItemSerializer(...):
    ...
    category = CategorySerializer()
    class Meta:
        ...
        fields = ['...',category]

# views.py
...
# this is to display ..
items = MenuItem.objects.select_related('category').all()

```
# 📑 Creating Models

- With Django ORM, you can work with models and databases without writing raw SQL queries.

# 📑 Example: Menu Model

```python
class Menu(models.Model):
    # These are the columns
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
```

# 📑 Handling Models in Django
## 1️⃣ First: Create Migrations
1. Add the model to INSTALLED_APPS in settings.py:
```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    ...
]

```
2. Run `python manage.py makemigrations` to create the migration file.
3. Apply the migration with `python manage.py migrate`.


## 2️⃣ Second: Access and Add Data
1.Start Python shell: `python manage.py shell`.
2. Import the model: `from myapp.models import Menu`
3. make ORM operations:
-  to create data:
```python 
n = Menu.objects.create(name='pasta', cuisine='italian', price=10)
```
- to Update data : 
```python
p = Menu.objects.get(pk=2)
p.price = 20
save()

```
- to Retrive data :
```python
Menu.objects.all()
```
- to Delete data :
```python
Menu.objects.get(pk=2).delete()
```

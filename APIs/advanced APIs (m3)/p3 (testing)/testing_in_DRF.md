## Django Testing Guide 🧪

### How Testing Works in Django ⚙️
Django provides a built-in testing framework based on Python’s `unittest` module. This allows you to create unit and integration tests to ensure your application works correctly. Testing helps you:

1. **Catch Bugs Early** 🐞 – Before deploying your code.
2. **Ensure Stability** 🔒 – Prevent breaking changes when modifying code.
3. **Automate QA** 🤖 – Run tests quickly instead of manually checking.

### Types of Tests in Django:
- **Model Tests** 🏗️: Ensure that models behave as expected.
- **View Tests** 👀: Check if views return the correct response.
- **Serializer Tests** 🔄: Ensure data is serialized correctly.
- **Form Tests** 📝: Validate form inputs.
- **Integration Tests** 🔗: Test multiple parts of the system together.

---

### Explanation of Your Code 📜

#### **1. Model (`Menu`)**
```python
from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {self.price}'
```
- Defines a `Menu` model with three fields: `title`, `price`, and `inventory`.
- `__str__` method returns a string representation in `"title : price"` format.

---

#### **2. Model Test (`test_models.py`)** 🧪
```python
from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=50, inventory=10)
        self.assertEqual(str(item), "IceCream : 50")
```
- `TestCase` is Django’s built-in testing class.
- `Menu.objects.create(...)` creates a test item in the database.
- `self.assertEqual(str(item), "IceCream : 50")` checks if the `__str__` method works correctly.

- 💡the `objects` manager deal directly with model, so u haven`t to create model intance.
- 💡we used `str(item)` cuz we compare it with `"some string"` .

---

#### **3. View Test (`test_views.py`)** 👀
```python
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="salad", price=10, inventory=45)
        Menu.objects.create(title="coffee", price=20, inventory=30)
        Menu.objects.create(title="water", price=5, inventory=100)

    def test_getall(self):
        url = reverse('menu/')
        res = self.client.get(url)

        menuitem = Menu.objects.all()
        serializer = MenuItemSerializer(menuitem, many=True)

        self.assertEqual(res.data, serializer.data)
        self.assertEqual(res.status_code, 200)
```
- `setUp()` method creates test data before running tests.
- `reverse('menu/')` generates the URL dynamically.
- `self.client.get(url)` makes a GET request.
- `self.assertEqual(res.data, serializer.data)` checks if response data matches expected data.
- `self.assertEqual(res.status_code, 200)` ensures the API returns status code `200`.

---

### Running Tests in Django 🚀
To run your tests, use:
```sh
python manage.py test
```
This will execute all test cases in your Django application.

---

### Summary 🏁
- **Model tests** ensure database logic works.
- **View tests** validate API responses.
- **Django’s test framework** is based on `unittest`.
- Use `python manage.py test` to run all tests.

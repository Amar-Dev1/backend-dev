# 📑 Django Admin

---

## 💡 Key Concepts:
- The **Django admin** is a **built-in dashboard** for administrators.
- It allows you to **add, update, delete, and manage models, users, permissions**, and more.
- You can **assign roles and permissions** to users and **track user activity history**.

---

## 🔥 How to Create an Admin Interface

### 1️⃣ **Create a Superuser**
To access the admin interface, you need to create a superuser account.

```bash
python manage.py createsuperuser
```

### 2️⃣ Register Your Models `admin.py`

```python 
from django.contrib import admin
from .models import MyModel  # Import your model

admin.site.register(MyModel)  # Register the model

```
### 3️⃣ Run the Server and Access the Admin Interface
```bash
python manage.py runserver
http://127.0.0.1:8000/admin/

```
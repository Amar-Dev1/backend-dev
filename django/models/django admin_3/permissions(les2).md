
# 📑 Permissions in Django

---

## 💡 **What Are Permissions?**
- Permissions **control which users are allowed to perform certain actions** (like create, read, update, or delete data) in Django.
- To allow users to perform a specific action, they **must be granted the necessary permissions**.

---

## 👥 **Types of Users in Django**
1. **Superuser** 🦸‍♂️ 
   - **Top-level admin** with **all permissions** by default.
   - Can **create, read, update, and delete** all data.
   - Can **add, update, delete users and manage permissions**.
   - Created using: 
     ```bash
     python manage.py createsuperuser
     ```

2. **Staff User** 👨‍💻
   - Can log in to the **admin dashboard**.
   - **Does not have permissions by default** to manage models.
   - Must be explicitly given permissions to **add, change, delete, or view data**.

3. **End User** 👤 
   - The regular user who interacts with the front-end or website.
   - **Cannot access the admin dashboard**.
   - **Cannot view, edit, or manage any data** by default.

---

## 📑 **Important Notes**
- The **superuser** is a staff user by default.
- **Staff users must be explicitly given permissions** (create, read, update, delete).
- **Users are marked as active by default**, so they can log in if they have valid credentials.

---

## 📑 **Creating Users and Assigning Status**
#### 🛠️ **1️⃣ Create a New User**
This can be done in the **Django shell**.

```python
from django.contrib.auth.models import User

# Create a new user (username, email, password)
user = User.objects.create_user('testuser', 'test@gmail.com', 'pass123')
```

#### 🛠️ 2️⃣ Set User as Staff
```python 
user.is_staff = True
user.save()
# 💡 This allows the user to log in to the admin dashboard, but they still don't have permissions to create, edit, or delete data.
```


## 📑 Check User Permissions
To check if a user has a specific permission, use has_perm().
```python 
user.has_perm('myapp.add_mymodel')
# 💡 This will return True if the user has permission to add MyModel, otherwise it returns False.
```

## 📑Django Groups
- 💡Django groups are used to assign permissions to multiple users at once.
- 💡Groups are useful when you have a large number of users with similar permissions.
- 💡You can assign a group to a user and the user will automatically get all the permissions.
- 💡You can also assign a user to multiple groups.

## 📑 **Summary of User Types and Permissions**

| **User Type**   | **Admin Access** | **Default Permissions**         | **CRUD (Create, Read, Update, Delete) Access** |
|-----------------|-----------------|---------------------------------|------------------------------------------------|
| **Superuser**    | ✅ Full access  | All permissions granted         | ✅ Full access to all data and users            |
| **Staff User**   | ✅ Admin access  | No permissions by default      | ❌ Must be explicitly granted permissions      |
| **End User**     | ❌ No access     | No permissions by default      | ❌ Cannot access admin site or manage data     |

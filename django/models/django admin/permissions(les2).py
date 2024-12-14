# 📑Permissions:->
# 💡it`s control which users are alowed to do which actions.
# 💡for users to perform a certain action, they need to get the permission to do that.


# 📑Users in Django:->
"""
1. superuser:-> A top-level administrator of the system and possesses permission to add, change, or delete other users, as well as perform operations on all the data in the project.
2. stff user:-> Allowed to access Dj admin interface, its doesn`t automatically get the permission to make create,read,update and delete the data.
3. user (end-user):-> Not authorized to user admin site.
"""

# 📑❗Note:->
"""
1. The superuser is a staff user (by default).
2. The staff user must given the permissions to manage the data.
3. The users are marked as active (by default).
"""

# 📑Creating users with status:->
"""
1️⃣Creating user (CMD):->
>>>> from django.contrib.auth.models import User
>>>> user = User.objects.create_user('testuser','test@gmail.com','pass123')

2️⃣Give him a status:->(for Ex: staff user):->
>>>> user.is_staff = True
>>>> user.save()
"""

# 📑Give a permissions:->
# 💡we can create permission using CMD or admin site.
"""
Examples:->
myapp.add_mymodel
myapp.change_mymodel
myapp.delete_mymodel
myapp.view_mymodel
"""

# 📑Check the users permissions:->
"""
>>>> user.has_perm('myapp.add_mymodel') => True or False
"""

# 📑Django Groups:->
"""
- 💡Django groups are used to assign permissions to multiple users at once.
- 💡Groups are useful when you have a large number of users with similar permissions.
- 💡You can assign a group to a user and the user will automatically get all the permissions.
- 💡You can also assign a user to multiple groups.
"""

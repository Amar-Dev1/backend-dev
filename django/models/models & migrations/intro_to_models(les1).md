# 📑 Model

- A model represents the structure of your database.
- Models replace custom SQL queries.
- Each model in Django corresponds to a table in the database.

# 📑 Note

- Django automatically creates a database table for each model.
- Each model attribute represents a database field.
- Django handles the primary key automatically, but you can override it.
- You can't create a database only by defining the model class; you need to use **migrations**.

# Some Model Methods

1. `save()`: Saves the model instance to the database (Create)  
   Example: `new_user.save()`

2. `get()`: Retrieves the model instance from the database (Read)  
   Example: `user = User.objects.get(id=1)`

3. `update()`: Updates the model instance in the database (Update)  
   Example: `user.name = "Ahmed Hassan"`

4. `delete()`: Deletes the model instance from the database (Delete)  
   Example: `user.delete()`

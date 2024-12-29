# 📑 ORM (Object Relational Mapping)

## 💡 What is ORM?
- **O**bject **R**elational **M**apping is a feature that automatically creates SQL queries using **Python syntax**.
- It acts as a **bridge** between the application and the **database**.
- It allows you to interact with the database using Python code instead of writing raw SQL queries.
- **Each row in the database** represents an **object** in ORM.

---

## 📑 Accessing the ORM
- ORM can be accessed via the **shell command**
  ```bash
  python manage.py shell
  ```


# 📑 QuerySet
- 💡 A QuerySet is a collection of objects (rows) from the database.
- 💡 It behaves like a list, but it’s dynamic — it can be filtered, sorted, and paginated.
- 💡 It represents the result of a database query.
- 💡 Django uses QuerySets to retrieve and manipulate objects from the database.


# 📑Examples
- SQL Query (Traditional):
```sql
SELECT * FROM Users WHERE name = "Amar";
```
- Django ORM :
```python
Users.objects.filter(name="Amar")
```

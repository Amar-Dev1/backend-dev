# 📑 Using Foreign Keys in Models

## 💡 Foreign Key:
- A **Foreign Key** is an ORM field used to create relationships between models.
- It establishes a **one-to-many** relationship between two models.

---

## 📑 Example:
Assume there is a **cafe** with the following models:
1. **Categories**
2. **Menu**
3. **Menu_Item**

To create a **one-to-many** relationship (where one menu has many menu items), a **Foreign Key** is used.

### 🔵 Implementation:
```python
class Menu_Item(models.Model):
    menu_id = models.ForeignKey(Menu, on_delete=models.PROTECT)
```
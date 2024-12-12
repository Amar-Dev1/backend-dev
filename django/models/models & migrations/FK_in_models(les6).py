# 📑Using Foreign Keys in models:->

# 💡Foreign Key :-> is ORM Field.
"""
assume that is a cafe contain these models :->
1. Categories
2. Menu
3. Menu_item

to make one to many relationship (menu to menu_items) i use Foreign Key field :->

in menu_item model :->
menu_id = models.ForeignKey(Menu,on_delete=models.PORTECT)
"""

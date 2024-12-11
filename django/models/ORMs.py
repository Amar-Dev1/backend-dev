# 📑ORM:->
# 💡Stand for object relational mapping
# 💡it`s a feature that automatically create SQL queries by language syntax (python syntax)
# 💡it`s like a bridge between the application and the database
# 💡it can be accessed by shell command

...

# 💡 each row in database represent object in ORM 💡

...


# 📑QuerySet:->
"""
💡 - A collection of objects (rows) in database
💡 - It`s like a list but it`s dynamic and can be filtered, sorted, pag
💡 - The result of a database query
💡 - Dj use it to retreive & manipulate the objects from database

"""

# 📑Examples:->
"""
SELECT * FROM Users WHERE name = "Amar" == Users.objects.filter(name="Amar")

"""

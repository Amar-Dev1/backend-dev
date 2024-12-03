# 📑Model :
"""
💡its a class that represents the structure of your database
💡we use model instead of custom queries in sql
💡Each model in dj app represents a table in database
"""

# 📑Note :
"""
💡 Dj automatically creates a database table for each model we define in our app
💡 Each attribute in model represent database field
💡 Dj automatically handle with the primary key (but we can override it)
💡 we can`t create a database only with defining model class , we need to use ⭕migrations⭕
"""

# some model methods :
# new_user = User(id=1,"Ahmed","Hassan")

"""
1. save() : saves the model instance to the database (Create) => new_user.save()
2. get() : returns the model instance from the database (Read) => user = User.objects.get(id=1)
3. update() : updates the model instance in the database (Update) => user.name = "Ahmed Hassan"
4. delete() : deletes the model instance from the database (Delete) => user.delete()

"""

# 📑Using Migrations :->

# 📑notes :->
"""
💡 Dj translate models into database tables using ⭕ migrations mechanism ⭕.
💡 Whenever I add a new model or effect changes in an existing model, I need to run the `makemigrations` command

"""

# 📑migrations commands :->
"""
1. makemigrations
2. migrate
3. sqlmigrate
4. showmigrations
"""

# 🔵information :->
"""
💡 When you create a Django project with the `startproject` command, certain apps are installed by default. These apps are listed in the INSTALLED_APPS section in the project’s settings.py file.
💡 Data needs to be stored via these apps for their functionality to work.
💡 Django uses the SQLite database by default. For that purpose, you run the `migrate` command.
"""

# 1️⃣ `makemigrations` command:->
"""
💡`makemigrations` is used to create new migration files for the models in the app.
💡It is achieved by writing : `python manage.py makemigrations`
"""

# 2️⃣ `migrate` command:->
"""
💡`migrate` is used to apply the tasks in the migrations file to be performed.
💡It is achieved by writing : `python manage.py migrate`

"""
# 3️⃣ `showmigrations` command:->
# 💡 when it run , it output will be like this :
"""
(django) C:\django\myproject>python manage.py showmigrations 
. . . 
. . . 
myapp 
[X] 0001_initial 
[ ] 0002_rename_name_person_person_name 
[ ] 0003_person_age 
. . . 

💡 X : refeer that the initial migration (file numbered 0001) has already migrated
which means => 0002 and 0003 files are pending

"""

# 4️⃣ `sqlmigrate` Command:->
"""
💡 `sqlmigrate` shows the SQL query or queries executed when a migration script is run.

"""

# How to undo the migrations ❓
"""
💡Run the `migrate` command and specify which migration file to be used so that the migrations after it will be undone or unapplied.

Example : 

(django) C:\django\myproject>python manage.py migrate myapp 0002_rename_name_person_person_name   

"""

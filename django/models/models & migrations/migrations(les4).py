# 📑Migrations :->
"""
💡 migrations are how Dj records changes made to models and implement these changes to the DBs schema ✅
💡 migrations stored into `Migrations file` in `Migrations folder` inside each app
💡 it`s help making (syncing, mintenance and version control for the models) :->

🚀 Syncing issues : it`s decrease the syncing issues possibility when working with a team
🚀 version control : all the changes are kept in version control (create history and help track changes)

"""

# 📑How Migrations work ? :->
"""
1. Create migrations script : `python manage.py makemigrations`
2. Apply the migrations : `python manage.py migrate`
"""

# 📑Migration Hisotory :->
"""
behind the scence, dj create migration table for tracking the changes applied in models =>
that let the devs control the version of the database ✅🚀 
"""

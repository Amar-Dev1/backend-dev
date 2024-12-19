# 📑 Migrations

- 💡 Migrations are how Django records changes made to models and implements these changes to the database schema ✅
- 💡 Migrations are stored in the `Migrations` folder inside each app.
- 💡 They help with (syncing, maintenance, and version control for the models): 

🚀 **Syncing issues**: Reduces syncing issues when working with a team.  
🚀 **Version control**: Keeps track of changes (creates a history and helps track changes).

# 📑 How Migrations Work?

1. Create migration script: `python manage.py makemigrations`
2. Apply the migrations: `python manage.py migrate`

# 📑 Migration History

- Behind the scenes, Django creates a migration table for tracking the changes applied to models.  
- This helps developers control the version of the database ✅🚀

# 📑 Using Migrations

## 📑 Notes:
- 💡 Django translates models into database tables using the ⭕ migrations mechanism ⭕.
- 💡 Whenever a new model is added or changes are made to an existing model, the `makemigrations` command must be run.

## 📑 Migrations Commands:
1. `makemigrations`
2. `migrate`
3. `sqlmigrate`
4. `showmigrations`

## 🔵 Information:
- 💡 When you create a Django project with the `startproject` command, certain apps are installed by default. These apps are listed in the `INSTALLED_APPS` section in the project’s settings.py file.
- 💡 Data needs to be stored via these apps for their functionality to work.
- 💡 Django uses the SQLite database by default. To apply migrations, you run the `migrate` command.

## 1️⃣ `makemigrations` Command:
- 💡 `makemigrations` is used to create new migration files for the models in the app.
- 💡 It is executed by running: `python manage.py makemigrations`

## 2️⃣ `migrate` Command:
- 💡 `migrate` is used to apply the tasks in the migration file to the database.
- 💡 It is executed by running: `python manage.py migrate`

## 3️⃣ `showmigrations` Command:
- 💡 When run, the output will show which migrations are applied or pending:
  ```bash
  (django) C:\django\myproject>python manage.py showmigrations
  ...
  myapp
  [X] 0001_initial
  [ ] 0002_rename_name_person_person_name
  [ ] 0003_person_age

  - 💡 [X] indicates that the migration has been applied, and [ ] indicates pending migrations.
  ...



# 4️⃣ `sqlmigrate` Command

💡 `sqlmigrate` shows the SQL query or queries executed when a migration script is run.

# How to undo the migrations ❓

- 💡Run the `migrate` command and specify which migration file to be used so that the migrations after it will be undone or unapplied.
```
(django) C:\django\myproject>python manage.py migrate myapp 0002_rename_name_person_person_name

```

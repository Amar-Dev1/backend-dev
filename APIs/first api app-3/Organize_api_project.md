# 📑Organize the API project

## ✅ To ensure the api project well structured
### 1️⃣ Split the app : 
- split your app into multiple apps.
### 2️⃣ Use virtual environment
- its good to use virtual environment to isolate the project dependencies.
### 3️⃣ Versioning
- create a new version of the app when upgrading the API
### 4️⃣ List dependencies
- list all the dependencies in the requirements.txt file.
### 5️⃣ Separate resource folders
- have a separate resource folder for each app
### 6️⃣ Multiple settings files
- split the settings into multiple settings files
### 7️⃣ Bussiness logic in models
- place the business logic into the models, instead of views

## 💡 what is pipenv
- pipenv is a tool that helps you to manage your project dependencies.
- it creates a virtual environment for your project and installs the dependencies in that environment.
- it also creates a requirements.txt file that lists all the dependencies of your project.

## 💡how to use pipenv
- install pipenv using pip install pipenv
- create a new project using pipenv install
- install the dependencies using pipenv install
- run the project using pipenv run python app.py

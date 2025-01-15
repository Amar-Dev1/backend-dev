# 📑 Configuring Django with MySQL

- 💡 To connect Dj with MySQL, we have to install mysqlclient package

## 1. Setup MySQL
1. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

2. **Install `mysqlclient`**
   ```bash
   pip install mysqlclient
   ```

3. **Connect to the MySQL server**
   ```bash
   mysql -u root -p
   ```
   - **Notes:**
     - Default port: `3306`. If different (e.g., `3307`), specify it with `-P`:
       ```bash
       mysql -u root -P 3307 -p
       ```
     - Default host: `localhost`. If different, specify it with `-h`:
       ```bash
       mysql -u root -h 127.0.0.1 -p
       ```

4. **Create the database**
   ```sql
   create database littlelemon;
   ```

5. **Verify the database**
   ```sql
   show databases;
   exit;
   ```

---

## 2. Configure Django Settings
1. **Update `settings.py`**
   Add the following to the `DATABASES` section:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'littlelemon',  # Your database name
           'USER': 'root',         # Your database user
           'PASSWORD': 'your_password',  # Your database password
           'HOST': '127.0.0.1',    # Your database host
           'PORT': '',             # Database port (leave empty for default 3306)
       }
   }
   ```

   ### Important Notes:
   - **Avoid using `root` in production.** Create a dedicated database user with limited permissions for better security.

---

## 3. Verify the Connection
1. **Run migrations** to create the necessary tables in the database:
   ```bash
   python manage.py migrate
   ```

2. **Check the database in MySQL shell**:
   ```sql
   use littlelemon;
   show tables;
   ```
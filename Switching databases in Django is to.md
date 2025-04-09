Switching databases in Django is totally doable — and Django makes it relatively smooth! Here's a clear step-by-step guide to switch from SQLite to MariaDB, preserving your existing data:

✅ Step-by-Step: Migrate Django from SQLite to MariaDB
🔧 1. Install MariaDB & Required Python Package
If MariaDB isn't installed:

bash
Copy
Edit
sudo apt install mariadb-server
Install the Python DB adapter:

bash
Copy
Edit
pip install mysqlclient
Make sure libmysqlclient-dev is installed (Linux):

bash
Copy
Edit
sudo apt-get install libmysqlclient-dev
🛠️ 2. Create a MariaDB Database & User
Log in to MariaDB:

bash
Copy
Edit
sudo mariadb
Inside the MariaDB shell:

sql
Copy
Edit
CREATE DATABASE myproject_db CHARACTER SET UTF8MB4;
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON myproject_db.* TO 'myuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
📁 3. Update settings.py
Replace your current DATABASES setting with:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject_db',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
🧱 4. Dump Data from SQLite
bash
Copy
Edit
python manage.py dumpdata > data.json
🧼 5. Delete SQLite DB and Migrate
Delete the db.sqlite3 file and all migrations if you want a clean slate (optional):

bash
Copy
Edit
rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
Now migrate to create MariaDB tables:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
📥 6. Load Your Data
bash
Copy
Edit
python manage.py loaddata data.json
🧪 7. Test Everything
Make sure your admin, models, and queries still work correctly.
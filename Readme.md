# 🚀 **Project Name: FlipFlow**

## 📄 **Overview**
**FlipFlow** is a comprehensive web application built with Django. It enables users to manage items, conduct transactions, and perform item analytics in an interactive and modern platform.

---
## 💻 **How to Run the Server**
To run the server on your local machine, follow these steps:
### 1.1 Just Clone the Repository:
```bash
git clone https://github.com/yourusername/flipflow.git
cd flipflow
```

### 1.2 Run "commands open server.py"
This is an automated python script which opens the venv and runs the server for you.
```python
import os
import webbrowser
import socket
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
webbrowser.open("http://{}:8000".format(IPAddr))
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)
print("Current working directory:", os.getcwd())

os.system('cmd /k "cd FlipFlow  & cd Scripts & activate & cd.. & cd Project & python manage.py runserver {}:8000"'.format(IPAddr))
```

### 1.3 case of dependancies error run
@FlipFlow\FlipFlow\Project
`pip install -r requirements.txt`

### 1.4 manual runserver
@FlipFlow\FlipFlow\
open terminal & write
`.\scripts\activate`
@FlipFlow\FlipFlow\Project
`python manage.py runserver`

Your application should now be running at `http://localhost:8000` or `http://<Your-IP-Address>:8000`.

---
## 🛠️ **Technologies Used**

- **Python 3.11+**
- **Django 4.x**
- **Django REST Framework**
- **SQLite3** (Default, pluggable with PostgreSQL/MySQL)
- **Bootstrap 5** (for frontend UI)
- **HTML & CSS**
- **JavaScript (Vanilla)**
- **Threading / Multiprocessing** (for periodic DB replication)
- **Git** (version control)

---
## ⚙️ **Key Features**

FlipFlow offers the following features to its clients:
1. **Secure accounting** using Django’s authentication system.
2. **Add, edit, or remove items** to be sold, each with price, description, quantity, and images.
3. **Deposit & withdraw cash** into your account to purchase items.
4. **Search for items** posted by other users.
5. **Purchase items from others**, transferring money and ownership.
6. **View full account info**:
   - Current cash balance
   - Purchased items
   - Sold items
   - Unsold inventory
8. **Inventory management dashboard**
9. **User and item analytics**, including statistics and charts.
10. **Robust REST API** to:
    - List, create, update, and delete items
    - Handle authorized transactions
    - Enable integration with external tools
11. **Batch add items via JSON API** (supports automation and integration)
12. **WSGI-threaded full DB replication** every 10 seconds for backup and fault tolerance

---

## 🌐 **Project Structure**

The FlipFlow project is divided into modular Django apps:
- **`Market`** – Handles item listing, purchases, and search
- **`Item`** – Manages individual item CRUD and media
- **`accounts`** – User registration, login, profile, and balance
- **`api`** – Exposes RESTful endpoints for all above features
Each app includes:
- `models.py` – Data schema
- `urls.py` – App routing
- `views.py` – Core business logic
- `templates/` – HTML templates
- `forms.py` – Input handling
- `api/serializers.py` – API serializers for DRF

---

## 📂 **Directory Structure Explanation**

accounts/               # User login, registration, profile
api/                    # API views and serializers
Item/                   # Item models, views, forms
Market/                 # Buying, selling, and marketplace logic
media/                  # Uploaded item images
Project/                # Django project settings and wsgi
static/                 # CSS, JS, and other static assets
templates/              # Shared templates (base, layout, etc.)
db.sqlite3              # Main database file
db_backups/             # Periodic DB backup storage
manage.py               # Django management script
requirements.txt        # Python dependencies

## 🎨 **Screenshots & Images**

**main view**
![[Screenshot 2025-05-10 001413.png]]
**profile view**
![[Screenshot 2025-05-10 000312.png]]

**inventory managment**

![[Screenshot 2025-05-10 001653.png]]
**api view**
![[Screenshot 2025-05-10 002807.png]]


---
## 🤝 **Contributing**

We welcome contributions!  
To contribute:

1. Fork this repository
    
2. Create a new branch (`git checkout -b feature/YourFeature`)
    
3. Commit your changes
    
4. Push to your branch (`git push origin feature/YourFeature`)
    
5. Create a Pull Request
---

**Thank you for checking out FlipFlow!** 🚀

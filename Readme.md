

---
```
  

{% extends "base.html" %}

{% block title %}ITEMS{% endblock %}

  

{% block body %}

{% load static %}

<div class="container">

    <h2 class="mb-4">Available Items</h2>

  

    <!-- Filter and Search Form -->

    <form method="get" class="mb-4">

        <div class="row">

            <div class="col-md-3">

                <!-- Search by Name -->

                <label for="name">Search by Name</label>

                {{ filter.form.name }}

            </div>

            <div class="col-md-3">

                <!-- Min Price -->

                <label for="min_price">Min Price</label>

                {{ filter.form.min_price }}

            </div>

            <div class="col-md-3">

                <!-- Max Price -->

                <label for="max_price">Max Price</label>

                {{ filter.form.max_price }}

            </div>



        </div>

        <button type="submit" class="btn btn-primary">Apply Filters</button>

    </form>

  

    <!-- Display Items -->

    <div class="row">

        {% for item in items %}

        <div class="col-md-4 mb-4">

            <div class="card shadow-sm">

                <div class="card-body">

                    <!-- Hyperlinked Item Name -->

                    <a href="{% url 'Item:item_detail' item.Item_slug %}" class="text-decoration-none">

                        <h5 class="card-title">{{ item.Item_name }}</h5>

                    </a>

                    <!-- Display Item Image if Exists -->

                    {% if item.Item_img %}

                    <img src="{{ item.Item_img.url }}" class="card-img-top" alt="Item Image" style="max-height: 200px; object-fit: cover;">

                    {% endif %}

                    <!-- Display Item Price -->

                    <p class="card-text"><strong>Price:</strong> ${{ item.Item_price }}</p>

  

                    <!-- Display Item Owner -->

                    <p class="card-text"><strong>Owner:</strong> {{ item.Item_owner.username }}</p>

  

                </div>

            </div>

        </div>

        {% empty %}

        <p class="text-muted">No items available.</p>

        {% endfor %}

    </div>

  

    <!-- Pagination -->

    <nav aria-label="Page navigation">

        <ul class="pagination justify-content-center">

            {% if items.has_previous %}

            <li class="page-item">

                <a class="page-link" href="?page=1">First</a>

            </li>

            <li class="page-item">

                <a class="page-link" href="?page={{ items.previous_page_number }}">Previous</a>

            </li>

            {% endif %}

  

            <li class="page-item disabled">

                <span class="page-link">Page {{ items.number }} of {{ items.paginator.num_pages }}</span>

            </li>

  

            {% if items.has_next %}

            <li class="page-item">

                <a class="page-link" href="?page={{ items.next_page_number }}">Next</a>

            </li>

            <li class="page-item">

                <a class="page-link" href="?page={{ items.paginator.num_pages }}">Last</a>

            </li>

            {% endif %}

        </ul>

    </nav>

</div>

{% endblock %}
```

**Item**
- models
	- Item
	- Category
- views
	- item_list
	- item_detail
	- item_create
	- item_update
	- item_delete
- forms
	- item_form
**Market**
- models
	- Transaction
- views
	- deposit
	- withdraw

	- place_offer

	- admin_pending_deposits
	-  approve_deposit
	- reject_deposit
	
	- inventory
	- sell

- forms
	- DepositForm
	- OfferForm
**accounts**
- models
	- Profile
- views
	- signup
	- profile
	- other_profile
	- profile_edit
	- del_account
- forms
	- SignupForm
	- UserForm
	- ProfileForm
---
#### 🔑 **Accounts (`/accounts/`)**
- `/profile/` → **User Profile**
- `/register/` → **Sign Up**
- `/profile/edit` → **Edit Profile**
- `/del_account/<slug>/` → **Delete Account**
- `/other_profile/<slug>/` → **View Other Profiles**
#### 🛒 **Market (`/Market/`)**
- `/deposit/` → **Deposit**
- `/withdraw/` → **Withdraw**
- `/admin/pending-deposits/` → **Pending Deposits**
- `/admin/approve-deposit/<id>/` → **Approve Deposit**
- `/admin/reject_deposit/<id>/` → **Reject Deposit**
- `/place_offer/<slug>/` → **Place Offer**
- `/inventory/` → **Inventory**
- `/sell/<id>/` → **Sell Item**
##### 🎨 **Items (`/`)**
- `/` → **Item List**
- `/<slug>/` → **Item Details**
- `/Item/item_create/` → **Create Item**
- `/Item/item_update/<slug>/` → **Edit Item**
- `/Item/item_delete/<slug>/` → **Delete Item**

---

```
git remote add origin https://github.com/minanasser54/FlipFlow.git
git branch -M main
git push -u origin main
```

iii. Add/Edit/remove Items to your account to be sold specifying the needed price.
iv. Deposit Cash into your account to purchase items.
v. Search for items for sale by other users. 
vi. Purchase item from another user, transfering money from your account to his account and transfering the item from your account to his account. 
vii. View your account info such as current cash balance , List of purchased items, list of sold items and items to be sold yet. viii. Mange inventory of the items. 
ix. Generate different kinds of reports such as reports about the transactions performed on the systems. 
x. Select at least three functionalities of this marketplace and implement them using SOAP or REST web services.
1. CRUD  to item
2. deposit / withdraw cash requests + admin handler
3. purchase / sell opertaions + cash auto transfer
4. searching & filters
5. Lists (bought / sold / to be sold)
6. Inventory managment
7. reports & analytics page



python3.12
```python
pip install -r requirements.txt
pip freeze > requirements.txt

F:\programfiles\Python\python.exe -m virtualenv FlipFlow
cd FlipFlow
.\Scripts\activate

pip install django
pip install pillow


django-admin startproject Project

python manage.py migrate
python manage.py createsuperuser  
	admin
	admin@admin.com
	123456789
python manage.py runserver


python manage.py startapp Item
#add app to settings.py
#after each database edit
python manage.py makemigrations
python manage.py migrate


```

#### item
- created db structure in **models.py**
- register in **admin.py**  
- makemigrations



**settings.py**
```python 
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = "/media/"
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')

TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': ['templates'],

        'APP_DIRS': True,

        'OPTIONS': {

            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

            ],

        },

    },

]
```

```
MinaNasserUsername
Mina2100370
```

```
1. `accounts/` `profile/ [name='profile']`
2. `accounts/` `register/ [name='signup']`
3. `accounts/` `profile/edit [name='profile_edit']`
4. `accounts/` `del_account/<slug:slug> [name='del_account']`
5. `admin/`
6. `[name='items']`
7. `<slug:slug>/ [name='item_detail']`
8. `accounts/` `login/ [name='login']`
9. `accounts/` `logout/ [name='logout']`
10. `accounts/` `password_change/ [name='password_change']`
11. `accounts/` `password_change/done/ [name='password_change_done']`
12. `accounts/` `password_reset/ [name='password_reset']`
13. `accounts/` `password_reset/done/ [name='password_reset_done']`
14. `accounts/` `reset/<uidb64>/<token>/ [name='password_reset_confirm']`
15. `accounts/` `reset/done/ [name='password_reset_complete']`
16. `^media/(?P<path>.*)$`
17. `^static/(?P<path>.*)$`
```

```{% extends "base.html" %}

  

{% block title %}ITEMS{% endblock %}

  

{% block body %}

{% load static %}

<div class="container">

    <h2 class="mb-4">Available Items</h2>

  

    <div class="row">

        {% for item in items %}

        <div class="col-md-4 mb-4">

            <div class="card shadow-sm">

                <div class="card-body">

                    <!-- Hyperlinked Item Name -->

                    <a href="{% url 'Item:item_detail' item.Item_slug %}" class="text-decoration-none">

                        <h5 class="card-title">{{ item.Item_name }}</h5>

                    </a>

                    <!-- Display Item Image if Exists -->

                    {% if item.Item_img %}

                    <img src="{{ item.Item_img.url }}" class="card-img-top" alt="Item Image" style="max-height: 200px; object-fit: cover;">

                    {% endif %}

                    <!-- Display Item Price -->

                    <p class="card-text"><strong>Price:</strong> ${{ item.Item_price }}</p>

  

                    <!-- Display Item Owner -->

                    <p class="card-text"><strong>Owner:</strong> {{ item.Item_owner.username }}</p>

  

                </div>

            </div>

        </div>

        {% empty %}

        <p class="text-muted">No items available.</p>

        {% endfor %}

    </div>

  

    <!-- Pagination -->

    <nav aria-label="Page navigation">

        <ul class="pagination justify-content-center">

            {% if items.has_previous %}

            <li class="page-item">

                <a class="page-link" href="?page=1">First</a>

            </li>

            <li class="page-item">

                <a class="page-link" href="?page={{ items.previous_page_number }}">Previous</a>

            </li>

            {% endif %}

  

            <li class="page-item disabled">

                <span class="page-link">Page {{ items.number }} of {{ items.paginator.num_pages }}</span>

            </li>

  

            {% if items.has_next %}

            <li class="page-item">

                <a class="page-link" href="?page={{ items.next_page_number }}">Next</a>

            </li>

            <li class="page-item">

                <a class="page-link" href="?page={{ items.paginator.num_pages }}">Last</a>

            </li>

            {% endif %}

        </ul>

    </nav>

</div>

{% endblock %}
```


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

```
{% extends "base.html" %}

{% block title %}Inventory{% endblock %}

{% block body %}

<div class="container mt-4">

    <h2>Your Inventory</h2>

    <h3>Items</h3>

    <ul>

        {% for item in items %}

            <li>

                {{ item.Item_name }} -

                {% if item.Item_published %}

                    <span class="text-success">Published</span>

                    <form method="POST">

                        {% csrf_token %}

                        <input type="hidden" name="item_id" value="{{ item.id }}">

                        <button type="submit" name="action" value="unpublish" class="btn btn-warning">Unpublish</button>

                    </form>

                {% else %}

                    <span class="text-danger">Unpublished</span>

                    <form method="POST">

                        {% csrf_token %}

                        <input type="hidden" name="item_id" value="{{ item.id }}">

                        <button type="submit" name="action" value="publish" class="btn btn-success">Publish</button>

                    </form>

                {% endif %}

                <h5>Pending Offers</h5>

                    <ul>

                        {% for offer in offers %}

                            {% if offer.items.id == item.id %}

                                <li>

                                    Offer of ${{ offer.amount }} for {{ offer.items.Item_name }} from {{ offer.user_from }}

                                    <a href="{% url 'Market:sell' offer.id %}" class="btn btn-primary">Review Offer</a>

                                </li>

                            {% endif %}

                        {% endfor %}

                    </ul>

            </li>

        {% endfor %}

    </ul>

  

</div>

{% endblock %}
```
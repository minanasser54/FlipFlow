

---
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

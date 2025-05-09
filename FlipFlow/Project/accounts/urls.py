from django.urls import path
from . import views
app_name='accounts'
urlpatterns=[
    path('profile/',views.profile,name='profile'),
    path('register/',views.signup,name='signup'),
    path('profile/edit',views.profile_edit,name='profile_edit'),
    path('del_account/<slug:slug>',views.del_account,name='del_account'),
    path('other_profile/<slug:slug>',views.other_profile,name='other_profile'),
    path('transaction_history/',views.transaction_history,name='transaction_history'),
    path('analytics/',views.analytics,name='analytics'),
    
]
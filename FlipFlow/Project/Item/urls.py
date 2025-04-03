from django.urls import include, path
from django.contrib import admin

from . import views
app_name = 'Item'
urlpatterns = [
    path('',views.item_list,name="item_list"),
    path('<slug:slug>/',views.item_detail,name="item_detail"),

]
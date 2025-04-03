from django.urls import include, path
from django.contrib import admin

from . import views
app_name = 'Item'
urlpatterns = [
    path('',views.item_list,name="item_list"),
    path('<slug:slug>/',views.item_detail,name="item_detail"),
    path('Item/item_create/',views.item_create,name="item_create"),
    path('Item/item_update/<slug:slug>',views.item_update,name="item_update"),
    path('Item/item_delete/<slug:slug>',views.item_delete,name="item_delete"),

]
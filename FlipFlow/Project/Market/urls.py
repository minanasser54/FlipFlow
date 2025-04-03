from django.urls import include, path
from django.contrib import admin

from . import views
app_name = 'Market'
urlpatterns = [
    path('deposit/',views.deposit,name='deposit'),
    path('withdraw/',views.withdraw,name='withdraw'),
    path('admin/pending-deposits/', views.admin_pending_deposits, name='admin_pending_deposits'),
    path('admin/approve-deposit/<int:transaction_id>/', views.approve_deposit, name='approve_deposit'),
    ]
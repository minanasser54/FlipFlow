
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet,TransactionViewSet
app_name = 'api'
router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
]
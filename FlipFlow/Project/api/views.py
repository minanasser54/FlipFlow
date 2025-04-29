from django.shortcuts import render
from rest_framework.permissions import IsAdminUser ,SAFE_METHODS, BasePermission,IsAuthenticated
from rest_framework import viewsets
from .serializers import ItemSerializer,TransactionSerializer
from Item.models import Item
from Market.models import Transaction


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_staff




class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_staff:
            return Item.objects.all()
        else:
            return Item.objects.filter(Item_owner=self.request.user)

        

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminOrReadOnly]
    def get_queryset(self):
        if self.request.user.is_staff:
            return Transaction.objects.all()
        else:
            return Transaction.objects.filter(user_from=self.request.user) | Transaction.objects.filter(user_to=self.request.user)
             
# Create your models here.
from django.db import models
from Item.models import Item
from django.contrib.auth.models import User
from django.utils import timezone

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('buy', 'Buy'),
    )
    TRANSACTION_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    user_from = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    transaction_status = models.CharField(max_length=10, choices=TRANSACTION_STATUS, default='pending')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    
    # Approval fields
    from_approve = models.BooleanField(default=False)
    to_approve = models.BooleanField(default=False)
    admin_approve = models.BooleanField(default=False)

    items = models.ManyToManyField(Item, blank=True)

    def __str__(self):
        return f"Transaction {self.id} type {self.transaction_type} from {self.user_from} to {self.user_to}"
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

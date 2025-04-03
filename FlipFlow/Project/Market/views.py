from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from accounts.models import Profile
from .forms import DepositForm
from django.contrib.auth import authenticate,login
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import datetime
from django.conf import settings
from django.utils.text import slugify
from Item.models import Item
from .models import Transaction
# Create your views here.
from django.contrib import messages


# Create your views here.
@login_required
def deposit(request):
    profile = Profile.objects.get(user=request.user)  # Get the logged-in user's profile
    if request.method == 'POST':
        depositform = DepositForm(request.POST)
        if depositform.is_valid():
            # Authenticate the user with the provided password
            password = depositform.cleaned_data['password']
            user = authenticate(username=request.user.username, password=password)
            if user:  # If authentication is successful
                # Get the deposit amount from the form
                deposit_amount = depositform.cleaned_data['amount']
                # Update the user's balance
                transaction = Transaction(
                    user_from=request.user,
                    user_to=request.user,  # Since it's a deposit, from_user and to_user are the same
                    transaction_type='deposit',
                    amount=deposit_amount,
                    from_approve=True, 
                    to_approve=True,
                    )
                transaction.save()
                # Show success message
                messages.success(request, "Deposit successful!")
                return redirect('/accounts/profile')  # Redirect to the profile page
            else:
                # If password is incorrect, show error
                messages.error(request, "Incorrect password. Please try again.")
        else:
            messages.error(request, "Invalid form data. Please check your input.")
    else:
        depositform = DepositForm()
    return render(request, 'deposit.html', {'profile':profile,'depositform': depositform})




@login_required
def withdraw(request):
    profile = Profile.objects.get(user=request.user)  # Get the logged-in user's profile
    if request.method == 'POST':
        depositform = DepositForm(request.POST)
        if depositform.is_valid():
            # Authenticate the user with the provided password
            password = depositform.cleaned_data['password']
            user = authenticate(username=request.user.username, password=password)
            if user:  # If authentication is successful
                # Get the deposit amount from the form
                deposit_amount = depositform.cleaned_data['amount']
            
                # Create a new transaction for the withdrawal
                transaction = Transaction(
                user_from=request.user,
                user_to=request.user,  # Since it's a deposit, from_user and to_user are the same
                transaction_type='withdraw',
                amount=deposit_amount,
                from_approve=True, 
                to_approve=True,
                )
                transaction.save()
                # Show success message
                messages.success(request, "withdraw successful!")
                return redirect('/accounts/profile')  # Redirect to the profile page
            else:
                # If password is incorrect, show error
                messages.error(request, "Incorrect password. Please try again.")
        else:
            messages.error(request, "Invalid form data. Please check your input.")
    else:
        depositform = DepositForm()
    return render(request, 'deposit.html', {'profile':profile,'depositform': depositform})





@login_required
def admin_pending_deposits(request):
    # Only allow admin users
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to view this page.")
        return redirect('home')  # Redirect to home or another appropriate page
    
    # Filter pending transactions of type 'deposit'
    pending_deposits = Transaction.objects.filter(
        (Q(transaction_type='deposit') | Q(transaction_type='withdraw')) & 
        (Q(transaction_status='pending') | Q(admin_approve=False))
    )
    context = {
        'pending_deposits': pending_deposits,
    }
    
    return render(request, 'admin/pending_transactions.html', context)

@login_required
def approve_deposit(request, transaction_id):
    # Only allow admin users
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to approve transactions.")
        return redirect('home')
    
    # Get the transaction object
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    if  transaction.transaction_status == 'pending' and transaction.from_approve==True and transaction.to_approve==True:
        # Approve the transaction
        transaction.admin_approve = True
        transaction.transaction_status = 'completed'
        profile = Profile.objects.get(user=transaction.user_to)
        if transaction.transaction_type=='deposit':
            profile.balance += transaction.amount
            profile.save()
        if transaction.transaction_type=='withdraw' and profile.balance >= transaction.amount:
            profile.balance -= transaction.amount
            profile.save()
        transaction.save()
        
        # Show success message
        messages.success(request, f"Deposit transaction {transaction.id} has been approved successfully.")
    else:
        # Show error message if transaction is not pending or not a deposit
        messages.error(request, "This transaction cannot be approved.")
    
    return redirect('Market:admin_pending_deposits')

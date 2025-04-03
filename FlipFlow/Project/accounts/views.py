from collections import defaultdict
from django.shortcuts import get_object_or_404, render,redirect
from django.core.paginator import Paginator
from .models import Profile
from .forms import SignupForm,UserForm,ProfileForm
from django.contrib.auth import authenticate,login
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from Market.models import Transaction
import datetime
from django.conf import settings
from django.utils.text import slugify
from Item.models import Item
# Create your views here.
from django.contrib import messages



def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            usname=form.cleaned_data['username']
            uspass=form.cleaned_data['password1']
            user=authenticate(username=usname,password=uspass)
            login(request,user)
            return redirect('/accounts/profile/edit')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

@login_required
def profile(request):
    profile=Profile.objects.get(user=request.user)
    items = Item.objects.filter(Item_owner=request.user, Item_published=True)
    Paginator_items=Paginator(items,2) # Show 10 items per page
    page_number=request.GET.get('page')
    items=Paginator_items.get_page(page_number)
    context={'profile':profile,'items':items}
    return render(request,'profile.html',context)


@login_required
def other_profile(request,slug):
    profile=Profile.objects.get(slug=slug)
    items = Item.objects.filter(Item_owner=profile.user, Item_published=True)
    Paginator_items=Paginator(items,2) # Show 10 items per page
    page_number=request.GET.get('page')
    items=Paginator_items.get_page(page_number)
    context={'profile':profile,'items':items}
    return render(request,'profile.html',context)

@login_required
def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,instance=profile.user)
        profileform=ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() & profileform.is_valid():
            slug=slugify(request.user)
            userform.save()
            myprofileform=profileform.save(commit=False)
            myprofileform.user=request.user
            myprofileform.slug=slug
            myprofileform.save()
            return redirect('/accounts/profile')
    else:
        userform=UserForm(instance=profile.user)
        profileform=ProfileForm(instance=profile)
    return render(request,'profile_edit.html',{'userform':userform,'profileform':profileform})


@login_required
def del_account(request,slug):
    profile=Profile.objects.get(Q(user=request.user)&Q(user=request.user))
    profile.delete()
    request.user.delete()
    return redirect('/')

@login_required
def transaction_history(request):
    profile = get_object_or_404(Profile, user=request.user)
# Transactions where the user is the buyer (bought items)
    bought_items = Transaction.objects.filter(
        user_from=request.user, 
        transaction_type="buy",
        transaction_status="completed"
    ).order_by('-created_at')

    # Transactions where the user is the seller (sold items)
    sold_items = Transaction.objects.filter(
        user_to=request.user, 
        transaction_type="buy",
        transaction_status="completed"
    ).order_by('-created_at')

    # Transactions that are pending for sale (offers received)
    to_be_sold = Transaction.objects.filter(
        user_to=request.user, 
        transaction_type="buy",
        transaction_status="pending"
    ).order_by('-created_at')

    context = {
        "profile": profile,
        "bought_items": bought_items,
        "sold_items": sold_items,
        "to_be_sold": to_be_sold
    }

    return render(request, "transaction_history.html", context)



@login_required
def analytics(request):
    profile = get_object_or_404(Profile, user=request.user)

    # Extend the timeframe to 90 days
    today = datetime.date.today()
    ninety_days_ago = today - datetime.timedelta(days=90)

    # Get transactions within the last 90 days
    transactions = Transaction.objects.filter(
        created_at__range=[ninety_days_ago, today],
        transaction_status="completed",
        admin_approve=True,
    )

    # Initialize tracking variables
    daily_balance = defaultdict(float)
    total_deposits = 0
    total_withdrawals = 0
    total_spent = 0
    total_earned = 0
    highest_earning_day = {"date": None, "amount": 0}
    highest_spending_day = {"date": None, "amount": 0}

    # Process transactions
    for transaction in transactions:
        date = transaction.created_at.date()
        amount = float(transaction.amount)

        if transaction.transaction_type == "deposit" and transaction.user_to == request.user:
            total_deposits += amount
            daily_balance[date] += amount

        elif transaction.transaction_type == "withdraw" and transaction.user_from == request.user:
            total_withdrawals += amount
            daily_balance[date] -= amount

        elif transaction.transaction_type == "buy":
            if transaction.user_from == request.user:  # Buyer (Expense)
                total_spent += amount
                daily_balance[date] -= amount
                if amount > highest_spending_day["amount"]:
                    highest_spending_day = {"date": date, "amount": amount}

            elif transaction.user_to == request.user:  # Seller (Revenue)
                total_earned += amount
                daily_balance[date] += amount
                if amount > highest_earning_day["amount"]:
                    highest_earning_day = {"date": date, "amount": amount}

    # Calculate net balance changes (Total Deposits + Earnings - Withdrawals - Spending)
    net_balance_change = (total_deposits + total_earned) - (total_withdrawals + total_spent)

    # Convert balance history to sorted list for chart rendering
    balance_chart_data = sorted(daily_balance.items())

    context = {
        "profile": profile,
        "total_deposits": total_deposits,
        "total_withdrawals": total_withdrawals,
        "total_spent": total_spent,
        "total_earned": total_earned,
        "net_balance_change": net_balance_change,
        "highest_earning_day": highest_earning_day,
        "highest_spending_day": highest_spending_day,
        "transactions": transactions,
        "today": today,
        "ninety_days_ago": ninety_days_ago,
        "balance_chart_data": balance_chart_data,
    }

    return render(request, "analytics.html", context)
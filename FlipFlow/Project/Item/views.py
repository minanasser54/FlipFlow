from django.shortcuts import render , get_object_or_404 ,redirect

from .filters import ItemFilter
from .models import Item, Category
from django.core.paginator import Paginator
from django.http import FileResponse, Http404,HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.db.models import Q
from accounts.models import Profile
from .forms import ItemForm
from Market.models import Transaction
# Create your views here.


def item_list(request):
    item_filter = ItemFilter(request.GET, queryset=Item.objects.filter(Item_published=True))
    items = item_filter.qs
    Paginator_items=Paginator(items, 4) # Show 10 items per page
    page_number=request.GET.get('page')
    items=Paginator_items.get_page(page_number)
    context={'items':items,
            'filter': item_filter
    }

    return render(request, 'Item/item_list.html',context)



def item_detail(request,slug):
    item=get_object_or_404(Item,Item_slug=slug)
    profile = item.Item_owner.profile
    
    # Get all transactions where this item was involved, either as 'user_from' or 'user_to'
    transactions = Transaction.objects.filter(items=item).order_by('-created_at')  # Order by latest transaction
# Prepare the ownership history by iterating through transactions
    ownership_history = []
    for transaction in transactions:
        if transaction.transaction_type == 'buy':  # Item was bought
            ownership_history.append({
                'seller': transaction.user_to,
                'buyer': transaction.user_from,
                'transaction_date': transaction.created_at,
                'amount': transaction.amount,
                'status': transaction.transaction_status
            })
        elif transaction.transaction_type == 'sell':  # Item was sold
            ownership_history.append({
                'seller': transaction.user_to,
                'buyer': transaction.user_from,
                'transaction_date': transaction.created_at,
                'amount': transaction.amount,
                'status': transaction.transaction_status
            })
    context = {
            'item': item,
            'profile': profile,
            'ownership_history': ownership_history,
        }
    return render(request,'Item/item_detail.html',context)

@login_required
def item_create(request):
    if request.method=='POST':
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.Item_owner=request.user
            myform.save()
            return redirect('/')
    else:
        form=ItemForm()
    categories=Category.objects.all()
    context={'form':form,
             'categories':categories}
    return render(request,'Item/item_create.html',context)

@login_required
def item_update(request,slug):
    item=get_object_or_404(Item,Item_slug=slug)
    if item.Item_owner==request.user:
        if request.method=='POST' :
            form=ItemForm(request.POST,request.FILES,instance=item)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.Item_owner=request.user
                myform.save()
                return redirect('/{}'.format(slug))
        else:
            form=ItemForm(instance=item)
        categories=Category.objects.all()
        context={'form':form,
                'categories':categories}
        return render(request,'Item/item_create.html',context)
    else:
        return redirect('/{}'.format(slug))

@login_required
def item_delete(request,slug):
    item=get_object_or_404(Item,Item_slug=slug)
    if item.Item_owner==request.user:
        item.delete()
        return redirect('/')

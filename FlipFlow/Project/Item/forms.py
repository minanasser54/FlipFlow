from django import forms
from .models import Item, Category

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['Item_name', 'Item_img', 'Item_description', 'Item_price', 'Item_quantity', 'Item_category', 'Item_published']
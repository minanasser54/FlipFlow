from django.db import models
from django.urls import reverse
import datetime
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
import os
from django.utils.timezone import now

def custom_upload_to(instance, filename):
    # Define a custom file naming scheme (e.g., based on user id and current timestamp)
    ext = filename.split('.')[-1]  # Get the file extension
    new_filename = f"{instance.id}_{now().strftime('%Y-%m-%d_%H-%M-%S')}.{ext}"
    return os.path.join('items_pics', str(instance.id), new_filename)

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str

# Create your models here.
class Item(models.Model):
    Item_name= models.CharField(max_length=100, verbose_name="Item Name")
    Item_img = models.ImageField(upload_to=custom_upload_to,blank=True,null=True)
    Item_owner=models.ForeignKey(User,blank=True, null=True,verbose_name=_("Item Owner"), on_delete=models.CASCADE,related_name='item_owner')
    Item_description= models.TextField(verbose_name="Item Description")
    Item_price= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Item Price")
    Item_quantity= models.IntegerField(verbose_name="Item Quantity")
    Item_published=models.BooleanField(_("Item Published"), default=False, help_text=_("Is this item published?"))
    Item_createdat=models.DateTimeField(_("Item Created At"), auto_now_add=True)
    Item_category=models.ForeignKey('Category',on_delete=models.CASCADE,blank=True,null=True)
    Item_slug = models.SlugField(blank=True,null=True,unique=True)
    
    # def get_absolute_url(self):
    #     return reverse('main:Item_detail',kwargs={'slug':self.slug})
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.Item_name
    
    def save(self,*args,**kwargs):
            if not self.Item_slug:
                self.Item_slug=slugify(self.Item_name)
                if not self.Item_slug:
                    self.Item_slug = arabic_slugify(self.Item_name)
            super(Item,self).save(*args , **kwargs)


class Category(models.Model):
    Category_name = models.CharField(max_length=100, verbose_name="Category Name")    
    Category_slug = models.SlugField(blank=True,null=True,unique=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def save(self,*args,**kwargs):
            if not self.Category_slug:
                self.Category_slug=slugify(self.Category_name)
                if not self.Category_slug:
                    self.Category_slug = arabic_slugify(self.Category_name)
            super(Category,self).save(*args , **kwargs)

    def __str__(self):
        return self.Category_name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})

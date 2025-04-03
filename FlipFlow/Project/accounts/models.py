from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django_countries.fields import CountryField
import datetime
import os
from django.db.models.signals import post_save
from django.utils.timezone import now

def custom_upload_to(instance, filename):
    # Define a custom file naming scheme (e.g., based on user id and current timestamp)
    ext = filename.split('.')[-1]  # Get the file extension
    new_filename = f"{instance.user.id}_{now().strftime('%Y-%m-%d_%H-%M-%S')}.{ext}"
    return os.path.join('profile_pics', str(instance.user.id), new_filename)

# Create your models here.
def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=custom_upload_to,blank=True,null=True)
    balance=models.DecimalField(max_digits=15,default=0, decimal_places=2, verbose_name="balance")
    slug = models.SlugField(blank=True,null=True)
    bio = models.TextField(blank=True)
    country = CountryField(blank=True)
    address = models.CharField(blank=True, max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    joindate = models.DateTimeField(blank=True, default=datetime.datetime.now)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
            if not self.slug:
                self.slug = arabic_slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
    def __str__(self):
        return f'{self.user.username} Profile'
     

    def get_absolute_url(self):
        return reverse('accounts:profile_detail',kwargs={'slug':self.slug})
    

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

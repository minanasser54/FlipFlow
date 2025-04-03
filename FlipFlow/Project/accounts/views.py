from django.shortcuts import render,redirect
from .models import Profile
from .forms import SignupForm,UserForm,ProfileForm
from django.contrib.auth import authenticate,login
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import datetime
from django.conf import settings
from django.utils.text import slugify

# Create your views here.



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
    
    context={'profile':profile}
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


def del_account(request,slug):
    profile=Profile.objects.get(Q(user=request.user)&Q(user=request.user))
    profile.delete()
    request.user.delete()
    return redirect('/')

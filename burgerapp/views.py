from django.shortcuts import render,redirect

from .forms import RegisterForm,LoginForm,UserProfileForm,ProfileUpdateForm

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    form = LoginForm()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request, 'accounts/login.html',{'form':form})

def profile(request):
    current_user = request.user
    
    profile = Profile.objects.filter(user_id = current_user.id).first()
    
    return render(request,'profile/profile.html',{"profile":profile})       

def editprof(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=request.user)
        form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if form.is_valid() and form.is_valid():
            form.save()
            form.save()
            return redirect('profile')
    else:
        form = UserCreationForm(instance = request.user)
        form = ProfileUpdateForm(instance = request.user.profile)
    return render(request,'profile/editprof.html',{'form':form})

def logout_user(request):
    logout (request)
    return redirect('login')        

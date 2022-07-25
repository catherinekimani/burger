from django.shortcuts import render,redirect

from .forms import RegisterForm,LoginForm

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
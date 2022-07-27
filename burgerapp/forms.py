from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1']
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_bio','user_profile']
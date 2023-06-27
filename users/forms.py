from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): #inherit from UserCreationForm
    email = forms.EmailField(required=True) #add email field

    class Meta: #gives us a nested namespace for configurations and keeps them in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #fields to show in form


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True) #add email field

    class Meta: #gives us a nested namespace for configurations and keeps them in one place
        model = User
        fields = ['username', 'email'] #fields to show in form

class ProfileUpdateForm(forms.ModelForm): #
    class Meta:
        model = Profile
        fields = ['image']
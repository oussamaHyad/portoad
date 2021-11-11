from django.contrib.auth import models
from django.forms import ModelForm, fields

#import the package taht gonna handle the user creation form
from django.contrib.auth.forms import UserCreationForm

# import our User Model to associate it with our form handler 
from django.contrib.auth.models import User


class UserRegistraition(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


from django import forms

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from Profile_app.models import *


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=12)
#     last_name = forms.CharField(max_length=10)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2',]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=12)
    last_name = forms.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

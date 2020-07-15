from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import CustomUser


class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm):
        model= CustomUser
        fields = UserCreationForm.Meta.fields + ('username','email','age',)

class CustomUserChange(UserChangeForm):
    class Mera(UserChangeForm):
        model = CustomUser
        fields = ('username','email','age',)

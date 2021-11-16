from typing import OrderedDict
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.db.models import fields
from django.forms import ModelForm
from django import forms
# from local.models import RegForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
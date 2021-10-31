from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from  .models import AccountDetail


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class AccountDetailForm(ModelForm):
    class Meta:
        model = AccountDetail
        fields = '__all__'

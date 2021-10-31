from django import forms
from django.forms import forms
from django.forms import ModelForm
from .models import BasicDetail

class Contactform(ModelForm):
    class Meta:
        model = BasicDetail
        fields = '__all__'


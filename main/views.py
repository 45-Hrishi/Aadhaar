from django.shortcuts import render, redirect
from .forms import Contactform
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
import requests


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():

            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response':recaptcha_response
            }
            body = {
                'username' : form.cleaned_data.get('username'),
                'firstname' : form.cleaned_data.get('first_name'),
                'last_name' : form.cleaned_data.get('last_name'),
                'address': form.cleaned_data.get('address'),
                'pincode':form.cleaned_data.get('pincode')
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
            result = r.json()
            print(result)
            
            if result['success']:
                form.save()
                messages.success(request, "Message sent." )
                # return redirect ("main:contact")
            messages.error(request, "Error. Message not sent.")

    form = Contactform()
    return render(request, "main/home.html", {'form':form, 'recaptcha_site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY})




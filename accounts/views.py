from django.shortcuts import render,redirect
from .forms import UserRegisterForm,AccountDetailForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import AccountDetail
from django.views.generic.edit import UpdateView

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            body = {'username' :form.cleaned_data.get('username'),
            'first_name' : form.cleaned_data.get('first_name'),
            'last_name' : form.cleaned_data.get('last_name'),
            'email' : form.cleaned_data.get('email'),
            }
            print(body)
            messages.success(request,'Registration Successful!!')
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return redirect('accounts:accountdetail')
    else:
      form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
    
@login_required
def Accountdetail(request):
    if request.method == "POST":
        form = AccountDetailForm(request.POST)
        if form.is_valid():
            form.save()
            body = {
                'address':form.cleaned_data.get('Address')
            }
            print(body)
            return redirect('main:home')
    else:
        form = AccountDetailForm()
    return render(request,'accounts/accountdetail.html',{'form':form})

class AddressUpdateView(UpdateView):
    model = Accountdetail
    fields = '__all__'
    success_url ="/"
    context_object_name = 'update'

def loginView(request):
    if request.method == "POST":
	    form = AuthenticationForm(request,request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request,user)
			    messages.info(request, f"You are now logged in as {username}.")
			    return redirect("main:home")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "accounts/login.html",{"login_form":form})

def logoutView(request):
    logout(request)
    messages.success(request,"You are Successfully Logout")
    return redirect('accounts:login')


    
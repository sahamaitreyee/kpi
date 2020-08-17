from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from urllib.parse import urlencode
from .models import Login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
import logging

# Create your views here.

def index(request):
    logging.debug(msg="in index")
    error_message=request.GET.get('error_message')
    print(error_message)
    form=AuthenticationForm()
    return render(request, 'dpproj/login.html',{"form":form,"error_messge":error_message})


def login_validation(request):
    logging.debug("in login_validation")
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        print(form.is_valid(), form.errors, type(form.errors))
        try:
            # check user exists in db
            user=Login.objects.get(user_name=form.cleaned_data.get('username'))
        except(KeyError,Login.DoesNotExist):
            return redirect('{}?{}'.format(reverse('dpproj:index'),urlencode({"error_message":"Register User"})))
        # check user exists in django auth model 
        authuser=authenticate(request,username=user.user_name, password=form.cleaned_data.get('password'))
        print(authuser is None)
        if authuser is None:
            return redirect('{}?{}'.format(reverse('dpproj:index'),urlencode({"error_message":"Invalid User"})))
        else:
            login(request,authuser)
            return redirect('dpproj:kpi', user=user.user_email)
    else:
        return redirect('dpproj:index')

def logout_user (request):
    logout(request)
    return redirect('dpproj:index')  

def kpi(request,user):
    if request.user.is_authenticated:
        return render(request, 'dpproj/kpi_main.html', {"user_email":user})
    else:
        return redirect('dpproj:index')
    



    

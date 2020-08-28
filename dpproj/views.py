from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .models import Login, Registration
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import logging
from dpproj.RegistrationForm import RegistrationForm, UploadFileForm
from collections import OrderedDict as SortedDict
import xlrd


# Create your views here.


def index(request):
    logging.debug(msg="in index")
    error_message = request.GET.get('error_message')
    print(error_message)
    form = AuthenticationForm()
    return render(request, 'dpproj/login.html', {"form": form, "error_messge": error_message})


def login_validation(request):
    logging.debug("in login_validation")
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid(), form.errors, type(form.errors))
        try:
            # check user exists in db
            user = Login.objects.get(
                user_name=form.cleaned_data.get('username'))
        except(KeyError, Login.DoesNotExist):
            return redirect('{}?{}'.format(reverse('dpproj:index'), urlencode({"error_message": "Register User"})))
        # check user exists in django auth model
        authuser = authenticate(
            request, username=user.user_name, password=form.cleaned_data.get('password'))
        print(authuser is None)
        if authuser is None:
            return redirect('{}?{}'.format(reverse('dpproj:index'), urlencode({"error_message": "Invalid User"})))
        else:
            login(request, authuser)
            return redirect('dpproj:kpi', user=user.user_email)
    else:
        return redirect('dpproj:index')


def logout_user(request):
    logout(request)
    return redirect('dpproj:index')


def kpi(request, user):
    if request.user.is_authenticated:
        return render(request, 'dpproj/kpi_home.html', {"user_email": user})
    else:
        return redirect('dpproj:index')


def kpi_registration(request, user):
    if request.user.is_authenticated:
        regis = RegistrationForm()
        return render(request, 'dpproj/kpi_registration.html', {"user_email": user, "form": regis})
    else:
        return redirect('dpproj:index')


def kpi_registration_complete(request, user):
    if request.user.is_authenticated:
        if request.method != 'POST':
            regis = RegistrationForm()
            return render(request, 'dpproj/kpi_registration.html', {"user_email": user, "form": regis})
        else:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                instance = form.save()
                # get properties as dict
                return render(request, 'dpproj/kpi_reg_complete.html', {"user_email": instance.email_add, "data": instance, "message": "Registation Successful"})
            else:
                return render(request, 'dpproj/kpi_registration.html', {"user_email": user, "form": form, "error_message": "Invalid Data"})
    else:
        return redirect('dpproj:index')


def kpi_upload(request, user):
    if request.user.is_authenticated:
        if request.method != 'POST':
            return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm()})
        else:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    # get the data as collection of sheets
                    for f in get_converted_data(request['FILE']):
                        # for each row in a single sheet
                        for data in f:
                            # expand the data from dict
                            r = Registration(**data)
                            r.save()
                    return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm(), "message": "excel upload successful"})
                except Exception:
                    return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm(), "message": "Invalid Excel"})
            else:
                return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm()})

    else:
        return redirect('dpproj:index')


def convert_to_dict(sheet):
    first_row = sheet.row(0)
    fields = map(lambda cell: cell.value, first_row)
    converted_data = []
    for rx in range(1, sheet.nrows):
        row = sheet.row(rx)
        if not row:
            continue
        values = map(lambda cell: cell.value, row)
        item_data = SortedDict(zip(fields, values))
        converted_data.append(item_data)
    return converted_data


def get_converted_data(excel_file):
    book = xlrd.open_workbook(
        file_contents=excel_file.read(), encoding_override='utf-8'
    )
    return [convert_to_dict(sheet) for sheet in book.sheets()]

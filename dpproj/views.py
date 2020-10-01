from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from urllib.parse import urlencode
from .models import Login, Registration, Employee
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import logging
from dpproj.RegistrationForm import RegistrationForm, UploadFileForm,SelectionForm
from dpproj.employeeForm import EmployeeForm
from collections import OrderedDict as SortedDict
from xlrd import open_workbook, xldate_as_tuple
from xlrd.sheet import XL_CELL_DATE
from datetime import date, datetime, time
from django.core import serializers
from .visualization import Visualization
from django.contrib.auth.models import User
import json

from bokeh.plotting import figure 
from bokeh.io import output_notebook, show



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
            user = Login.objects.get(user_name=form.cleaned_data.get('username'))
        except(KeyError, Login.DoesNotExist):
            return render(request, 'dpproj/login.html',{"form":form,"error_message": "Register User"})
        # check user exists in django auth model
        authuser = authenticate(
            request, username=user.user_name, password=form.cleaned_data.get('password'))
        print(authuser is None)
        if authuser is None:
            return render(request,'dpproj/login.html',{"form":form,"error_message": "Invalid User"})
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
        return render(request, 'dpproj/kpi_home.html', {"user_email": user,  "data": Registration.objects.count()})
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
                save_data=serializers.serialize('json',Registration.objects.filter(pk=instance.id))
                j=json.loads(save_data)
                # get properties as dict
                return render(request, 'dpproj/kpi_reg_complete.html', {"user_email": user, "data":j[0]['fields'], "message": "Registation Successful", "form":RegistrationForm()})
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
                error=[]
                count=0
                try:
                    # get the data as collection of sheets
                    for f in get_converted_data(request.FILES['file']):
                        # for each row in a single sheet
                        for data in f:
                            count=count+1
                            d=RegistrationForm(data, instance=Registration())
                            if(d.is_valid()):
                                d.save()
                            else:
                                error.append("Row{}.{}".format(count,d.errors))
                except Exception as e:
                    return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm(), "message": "Invalid Excel.{}".format(e)})
                else:
                    if len(error)>0:
                        return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm(), "error_message": "Falied for Some row.{}".format(error)})
                    else:
                        return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm(), "message": "excel upload successful"})
            else:
                return render(request, 'dpproj/kpi_upload.html', {"user_email": user, "form": UploadFileForm()})

    else:
        return redirect('dpproj:index')

def get_visualization(request, user):
    if request.user.is_authenticated:
        if request.method != 'POST':
            return render(request, 'dpproj/kpi_visualization.html', {"user_email": user, "form": SelectionForm()})
        else:
            try:
                form = SelectionForm(request.POST)
                choice=""
                if(form.is_valid()):
                    choice=form.cleaned_data['selection']
                content=""
                v=Visualization()
                if(choice=='BAR'):
                    content=v.get_bar_plots(fields=['last_passout_year','it_exp_months','state_location'])
                else:
                    content=v.get_charts(fields=['gender','graduate_stream','pg_stream'])
                
            except Exception  as e:
                return render(request,'dpproj/kpi_visualization.html', 
                    {
                        "user_email":user,
                        "error_message": "Some error while getting visualization {}".format(e),
                        "form":SelectionForm()
                    }
                )

        return render(request, 'dpproj/kpi_visualization.html', {'user_email':user,"data":content, "form":SelectionForm() })
    else: 
        return redirect('dpproj:index')

def kpi_employee_regis(request, user):
    if request.user.is_authenticated:
        if request.method!='POST':
            #prepopulate the data with user name
            regis = EmployeeForm({'username':user},instance=Employee()) 
            return render(request, 'dpproj/kpi_employee.html', {"user_email": user, "form": regis})
        else:
            form =EmployeeForm(request.POST)
            if form.is_valid():
                u=User.objects.get(username=form.cleaned_data.get('username'))
                u.set_password(form.cleaned_data.get('newpassword'))
                u.save()
                form.fields['newpassword'].initials=''
                instance=form.save()
                save_data=serializers.serialize('json',Employee.objects.filter(pk=instance.id))
                j=json.loads(save_data)
                # get properties as dict
                return render(request, 'dpproj/kpi_reg_complete.html', {"user_email": user, "data":j[0]['fields'], "message": "Update Successful", "form":RegistrationForm()})
            else:
                return render(request, 'dpproj/kpi_employee.html', {"user_email": user, "form": form, "error_message": "Invalid Data"})

    else:
        return redirect('dpproj:index')

#helper functions 
def convert_to_dict(sheet):
    first_row = sheet.row(0)
    fields = list(map(lambda cell: cell.value, first_row[1:])) #skip first column
    converted_data = []
    print(sheet.nrows)
    for rx in range(1, sheet.nrows):
        row = sheet.row(rx)
        if not row:
            continue
        values = list(map(lambda cell: datetime(*xldate_as_tuple(cell.value, sheet.book.datemode)) if cell.ctype==XL_CELL_DATE else cell.value, row[1:]))
        item_data = SortedDict(zip(fields, values))
        converted_data.append(item_data)
    return converted_data


def get_converted_data(excel_file):
    book = open_workbook(
        file_contents=excel_file.read(), encoding_override='utf-8'
    )
    return [convert_to_dict(sheet) for sheet in book.sheets()]

    
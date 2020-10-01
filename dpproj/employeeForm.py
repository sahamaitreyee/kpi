from django.forms import ModelForm
from .models import Employee
from django import forms
from django.utils.translation import gettext_lazy as _


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        locallized_fields = '__all__'
        widgets={
            'newpassword': forms.PasswordInput(),
            'username':forms.TextInput(attrs={'readonly':'readonly'})
        }
        labels = {
            'username':_('User Name'),
            'employeeId':_('Employee ID'),
            'name': _('Employee Name'),
            'email': _('Email'),
            'designation':_('Designation'),
            'department':_('Department'),
            'newpassword':_('New Password')
        }
from django.forms import ModelForm
from .models import Registration
from django import forms
from django.utils.translation import gettext_lazy as _

class RegistrationForm(ModelForm):
    class Meta:
        model=Registration
        fields='__all__'
        locallized_fields='__all__'
        labels={
            'user_name':_('Candidate Name'),
            'user_last_name':_('Candidate Surname'),
            'user_dob':_('Date Of Birth'),
            'user_gender':_('Gender'),
            'aadhar_card':_('Aadhar Card No'),
            'joining_date':_('Date of Joining'),
            'last_passout_year':_('Passout Year'),
            'graduate_degree':_('Graduate Degree'),
            'pg_degree':_('PG Degree'),
            'graduate_stream':_('Graduate Stream'),
            'pg_stream':_('PG Stream'),
            'pg_yes_or_no':_('PG Available'),
            'it_exp_months':_('IT Exp (Months)'),
            'non_it_exp_months':_('NON IT Exp (Months)'),
            'freshers':_('Freshers')
        }

class UploadFileForm(forms.Form):
    file = forms.FileField()    

from django.forms import ModelForm
from .models import Registration
from django import forms
from django.utils.translation import gettext_lazy as _


class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        locallized_fields = '__all__'
        widgets={
            'dob':forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
            'joining_date': forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
            'feedback':forms.Textarea()
        }
        labels = {
            'name': _('Candidate Name'),
            'dob': _('Date Of Birth'),
            'gender': _('Gender'),
            'aadhar_card_number': _('Aadhar Card No'),
            'joining_date': _('Date of Joining'),
            'last_passout_year': _('Passout Year'),
            'graduate_degree': _('Graduate Degree'),
            'pg_degree': _('PG Degree'),
            'graduate_stream': _('Graduate Stream'),
            'pg_stream': _('PG Stream'),
            'pg_yes_or_no': _('PG Available'),
            'it_exp_months': _('IT Exp (Months)'),
            'non_it_exp_months': _('Non IT Exp (Months)'),
            'freshers': _('Freshers'),
            'feedback':_('Feedback')

        }
      

class UploadFileForm(forms.Form):
    file = forms.FileField()    

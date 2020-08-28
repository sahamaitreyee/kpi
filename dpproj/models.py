from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Login(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=20)
    def __str__(self):
        return self.user_name

class Answer(models.IntegerChoices):
    NO = 0, _('No')
    YES = 1, _('Yes')

    __empty__ = _('(Unknown)')

class Registration(models.Model):
    
    identity_list=(
        ('p','PAN CARD'),
        ('v','VOTER CARD'),
        ('d','DRIVING LISCENCE'),
        ('a','AADHAR CARD')
    )

    gender_info=(
        ('m','male'),
        ('f','female')
    )

    deg_info=(
        ('bba','Bachelors of Business Admin.'),
        ('bse','Bachelors of Science'),
        ('be','Bachelors of Engineering'),
        ('bca','Bachelors of Comp. Application')
    )

    pg_deg_info=(
        ('me','Master of Engineering'),
        ('mca','Master of Comp. Application'),
        ('mba','Master of Business Admin.'),
        ('mstat','Master of Stat')
    )
    stream=(
        ('ECE','Electronice & Communication'),
        ('EEE', 'Electrical Engineering'),
        ('CS','Computer Scienec'),

    )
    
    user_name=models.CharField(max_length=20)
    user_last_name=models.CharField(max_length=50)
    user_dob=models.DateTimeField()
    user_gender=models.CharField(max_length=1, choices=gender_info, blank=False)
    aadhar_card_no=models.CharField(max_length=16)
    joining_date=models.DateTimeField()
    last_passout_year=models.IntegerField()
    graduate_degree=models.CharField(max_length=6,default='others',choices=deg_info, blank=False)
    pg_degree=models.CharField(max_length=6, default='not done', choices=pg_deg_info, blank=False)
    graduate_stream=models.CharField(max_length=8, default='NOT FOUND', choices=stream, blank=False)
    pg_stream=models.CharField(max_length=8, default='NOT FOUND', choices=stream, blank=False)
    pg_yes_or_no=models.CharField(max_length=3, choices=Answer.choices)
    it_exp_months=models.IntegerField()
    not_it_exp_months=models.IntegerField()
    freshers=models.IntegerField(choices=Answer.choices)

    def __str__(self):
        return '{}.{}'.format(self.user_name,self.user_last_name)
    class Meta:
        ordering=['user_name']

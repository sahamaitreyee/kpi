from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.serializers.json import DjangoJSONEncoder
# Create your models here.
class Login(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=20)
    def __str__(self):
        return self.user_name

class Answer(float, models.Choices):
    NO = 0.0, _('No')
    YES = 1.0, _('Yes')
    (Unknown)=-1.0,_('(Unknown)')

class Registration(models.Model):
    
    identity_list=(
        ('p','PAN CARD'),
        ('v','VOTER CARD'),
        ('d','DRIVING LISCENCE'),
        ('a','AADHAR CARD')
    )

    gender_info=(
        ('male','male'),
        ('female','female')
    )

    deg_info=(
        ('bba','Bachelors of Business Admin.'),
        ('bsc','Bachelors of Science'),
        ('be','Bachelors of Engineering'),
        ('bca','Bachelors of Comp. Application'),
        ('others','Others')
    )

    pg_deg_info=(
        ('me','Master of Engineering'),
        ('mca','Master of Comp. Application'),
        ('mba','Master of Business Admin.'),
        ('mstat','Master of Stat'),
        ('not done','NA')
    )
    stream=(
        ('ECE','Electronice & Communication'),
        ('EEE', 'Electrical Engineering'),
        ('CS','Computer Scienec'),
        ('NOT FOUND','Not Applicable')
    )
    yes_no=(
        ('yes','Yes'),
        ('no','No')
    )
    
    name=models.CharField(max_length=20)
    dob=models.DateField()
    gender=models.CharField(max_length=6, choices=gender_info, default='female', blank=False)
    aadhar_card_number=models.CharField(max_length=16)
    joining_date=models.DateField()
    last_passout_year=models.IntegerField()
    graduate_degree=models.CharField(max_length=6,default='others',choices=deg_info, blank=False)
    pg_degree=models.CharField(max_length=8, default='not done', choices=pg_deg_info, blank=False)
    graduate_stream=models.CharField(max_length=9, default='NOT FOUND', choices=stream, blank=False)
    pg_stream=models.CharField(max_length=9, default='NOT FOUND', choices=stream, blank=False)
    pg_yes_or_no=models.CharField(max_length=3,choices=yes_no, default='no')
    it_exp_months=models.IntegerField()
    non_it_exp_months=models.IntegerField()
    freshers=models.FloatField(choices=Answer.choices, default=Answer.NO)

    def __str__(self):
        return '{}.{}.{}'.format(self.name,self.joining_date,self.graduate_degree)
    class Meta:
        ordering=['name']

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
        ('bcom','Bachelors of Commerce'),
        ('bstat','Bachelors of Statistics'),
        ('b.tech','Bachelors of Technology'),
        ('others','Others'),
        ('not found','Not found')
    )

    pg_deg_info=(
        ('me','Master of Engineering'),
        ('mca','Master of Comp. Application'),
        ('mba','Master of Business Admin.'),
        ('mstat','Master of Stat'),
        ('not done','NA'),
        ('msc','Master of Science'),
        ('mca','Master of Computer Application'),
        ('others','others'),
        ('mtech','Master of Technology'),
        ('mcom','Master of Commerce')
    )
    stream=(
        ('ECE','Electronice & Communication'),
        ('EE', 'Electrical Engineering'),
        ('CS','Computer Scienec'),
        ('NOT FOUND','Not Applicable'),
        ('No Stream','No Stream')
    )
    yes_no=(
        ('yes','Yes'),
        ('no','No')
    )   
    yes_no_Cap=(
        ('Yes','Yes'),
        ('No','No')
    ) 
    yes_no_notfound=(
        ('Yes','YES'),
        ('No','NO'),
        ('NOT FOUND','NOT FOUND')
    )
    state=(
        ('West Bengal','West Bengal'),
        ('Bihar','Bihar'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Haryana','Haryana'),
        ('Odisa','Odisa'),
        ('Rajasthan','Rajasthan'),
        ('Karnataka','Karnataka'),
        ('Andhrapradesh','Andhra Pradesh'),
        ('Jharkhand','Jharkhand'),
        ('Delhi','Delhi'),
        ('Ladakh','Ladakh'),
        ('Punjab','Punjab'),
        ('Himachal Pradesh','Himachal Pradesh'),
        ('Telangana','Telangana'),
        ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
        ('Maharashtra','Maharashtra'),
        ('Jammu and Kashmir','Jammu and Kashmir'),
        ('Assam','Assam'),
        ('Odisha','Odisha')
    )
    
    interest_choices=(
        ('Python','Python'),
        ('Java','Java'),
        ('Data Science','Data Science')
    )
    fathers_occupations=(
        ('PrivateBusiness','Private Business'),
        ('NotFound','Not Found'),
        ('Retired Govt. Employee','Retired Govt. Employee'),
        ('Retired in Defence','Retired in Defence')
    )
    mothers_occupation=(
        ('Teacher','Teacher'),
        ('Homemaker','Homemaker'),
        ('NotFound','Not Found')
    )
    social_ref=(
        ('Facebook','Facebook'),
        ('LinkedIn','LinkedIn'),
        ('Consultancy','Consultancy'),
        ('Others','Others')
    )
    joining_status=(
        ('Called for HR Round','Called For HR Round'),
        ('HR Round Complete','HR Round Completed'),
        ('Direct joining','Direct Joining'),
        ('Confirmed but not join','Confirmed but not join')
    )

    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=6, choices=gender_info, default='female', blank=False)
    aadhar_card_number=models.CharField(max_length=16)
    joining_date=models.DateField()
    last_passout_year=models.IntegerField()
    graduate_degree=models.CharField(max_length=10,default='others',choices=deg_info, blank=False)
    pg_degree=models.CharField(max_length=8, default='not done', choices=pg_deg_info, blank=False)
    graduate_stream=models.CharField(max_length=9, default='NOT FOUND', choices=stream, blank=False)
    pg_stream=models.CharField(max_length=9, default='NOT FOUND', choices=stream, blank=False)
    pg_yes_or_no=models.CharField(max_length=3,choices=yes_no, default='no')
    it_exp_months=models.IntegerField()
    non_it_exp_months=models.IntegerField()
    freshers=models.FloatField(choices=Answer.choices, default=Answer.NO)
    marks_10th_percent=models.FloatField()
    marks_12th_percent=models.FloatField()
    graduate_cgpa=models.FloatField()
    pg_cgpa=models.FloatField()
    aptitude_score=models.IntegerField(default=0)
    have_laptop=models.CharField(max_length=10,choices=yes_no_notfound, default='No')
    state_location=models.CharField(max_length=30,choices=state,blank=False)
    district_location=models.CharField(max_length=30, default='na')
    purpuse_of_visit=models.CharField(max_length=10,choices=(('CLP','CLP'),('Internship','Internship')), default='Internship')
    college_name=models.CharField(max_length=50, blank=True)
    pg_college=models.CharField(max_length=50, blank=True)
    domain_interested=models.CharField(max_length=15,choices=interest_choices, default='Python')
    fathers_occupation=models.CharField(max_length=50,choices=fathers_occupations, default='NotFound')
    mothers_occupation=models.CharField(max_length=50,choices=mothers_occupation, default='NotFound')
    no_of_siblings=models.CharField(max_length=10,default='NotFound')
    siblings_working=models.CharField(max_length=10,default='NotFound')
    domain_knowledge=models.CharField(max_length=10,choices=yes_no_Cap, default='No')
    previous_interviews_no=models.CharField(max_length=10,default='NotFound')
    selected_interviews=models.CharField(max_length=10,default='NotFound')
    reference_source=models.CharField(max_length=30,choices=social_ref, blank=False)
    status=models.CharField(max_length=100,choices=joining_status)
    joined_yes_no=models.CharField(max_length=3,choices=yes_no,default='no',blank=True)
    phone_number=models.IntegerField()
    mail_id=models.EmailField(default='a@a.com')
    feedback=models.CharField(max_length=100)
    

    def __str__(self):
        return '{}.{}.{}'.format(self.name,self.joining_date,self.graduate_degree)
    class Meta:
        ordering=['name']

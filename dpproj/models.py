from django.db import models

# Create your models here.
class Login(models.Model):
    user_name=models.CharField(max_length=20)
    user_email=models.CharField(max_length=20)
    def __str__(self):
        return self.user_name
from django.contrib import admin

# Register your models here.
from .models import Login,Registration
admin.site.register(Login)
admin.site.register(Registration)


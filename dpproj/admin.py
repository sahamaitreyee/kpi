from django.contrib import admin

# Register your models here.
from .models import Login,Registration,Employee
admin.site.register(Login)
admin.site.register(Registration)
admin.site.register(Employee)


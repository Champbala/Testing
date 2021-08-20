from Register.models import Registeration
from django.contrib import admin
from .models import Department, Registeration
# Register your models here.

admin.site.register(Registeration)

admin.site.register(Department)

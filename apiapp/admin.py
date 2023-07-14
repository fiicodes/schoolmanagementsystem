from django.contrib import admin

# Register your models here.
from django.contrib import admin
from adminapp.models import *

# Register your models here.
admin.site.register(subject_tb)
admin.site.register(course_tb)
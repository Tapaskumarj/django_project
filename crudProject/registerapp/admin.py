from django.contrib import admin
from .models import crud_student

# Register your models here.
@admin.register(crud_student)
class crud_studentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','sroll','course','doj','dob','gender','state','nationality','mob','email']
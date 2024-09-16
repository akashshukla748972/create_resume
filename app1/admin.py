from django.contrib import admin
from app1.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']

admin.site.register(Student, StudentAdmin)

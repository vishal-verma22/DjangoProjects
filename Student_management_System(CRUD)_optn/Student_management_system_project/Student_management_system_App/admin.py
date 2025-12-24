from django.contrib import admin
from .models import StudentModel
# Register your models here.

class AdminCustomization(admin.ModelAdmin):
	list_display=("name","rollno","subject","mark")

admin.site.register(StudentModel,AdminCustomization)

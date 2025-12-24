from django.contrib import admin
from .models import DepartmentModel,StudentModel

# Register your models here.
	
class DepartmentModelCustomization(admin.ModelAdmin):
	list_display=("Dept_id","Dept_name")
	
class StudentModelCustomization(admin.ModelAdmin):
	list_display=("name","rollno")


admin.site.register(DepartmentModel,DepartmentModelCustomization)
admin.site.register(StudentModel,StudentModelCustomization)



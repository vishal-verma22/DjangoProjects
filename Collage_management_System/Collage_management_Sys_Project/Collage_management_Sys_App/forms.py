from django import forms
from .models import DepartmentModel,StudentModel

class DepartmentModelForm(forms.ModelForm):
	class Meta:
		model=DepartmentModel
		fields="__all__"

class StudentModelForm(forms.ModelForm):
	class Meta:	
		model=StudentModel
		fields="__all__"
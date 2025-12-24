from django import forms

class DocumentForm(forms.Form):
	name=forms.CharField()
	Rollno=forms.IntegerField()
	marksheet=forms.FileField()
	Id_Card=forms.FileField()
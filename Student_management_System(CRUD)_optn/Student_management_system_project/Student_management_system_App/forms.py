from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
            'rollno': forms.NumberInput(attrs={'size': 20}),
            'subject': forms.TextInput(attrs={'size': 30}),
            'mark': forms.TextInput(attrs={'size': 30}),
        }

    # Name validation
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 2:
            raise forms.ValidationError("Name should contain minimum 2 alphabets")
        return name

    # Roll number validation
    def clean_rollno(self):
        rno = self.cleaned_data.get("rollno")

        # Check number only
        if not str(rno).isdigit():
            raise forms.ValidationError("Rollno should contain number only")

        # Check minimum value
        if int(rno) <= 0:
            raise forms.ValidationError("Rollno should be minimum 1")
        
        return rno

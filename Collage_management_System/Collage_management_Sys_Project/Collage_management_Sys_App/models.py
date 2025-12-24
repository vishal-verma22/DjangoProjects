from django.db import models

# Create your models here.

class DepartmentModel(models.Model):
	Dept_id=models.IntegerField(primary_key=True)
	Dept_name=models.CharField(max_length=40)
	
	def __str__(self):
		return self.Dept_name

class StudentModel(models.Model):
	name=models.CharField(max_length=40)
	rollno=models.IntegerField(primary_key=True)
	Branch=models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.rollno)
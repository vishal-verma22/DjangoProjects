from django.shortcuts import render,get_object_or_404,redirect
from .models import DepartmentModel,StudentModel
from .forms import DepartmentModelForm,StudentModelForm

# Create your views here.

def home(request):
	return render(request,"home.html")


def create_dept(request):
	if request.method=="POST":
		data=DepartmentModelForm(request.POST)
		if data.is_valid():
			data.save()
			msg="Department Created succesfully"
			return render(request,"createDepartment.html",{"message":msg,"form":data})
		else:
			msg="Check error"
			return render(request,"createDepartment.html",{"message":msg,"form":data})
	

	else:
		frm_obj_varble=DepartmentModelForm()
		return render(request,"createDepartment.html",{"form":frm_obj_varble})


def view_dept(request):
	model=DepartmentModel.objects.all()
	return render(request,"Viewdepartment.html",{"model":model})

def delete_dept(request,id):
	data=get_object_or_404(DepartmentModel,Dept_id=id)
	if request.method=="POST":
		data.delete()
		return redirect("view_dept")
	else:
		return render(request,"deleteDepartment.html",{"received_data":data})


def Create_student(request):
	form_obj_varble=StudentModelForm()

	if request.method=="POST":
		data=StudentModelForm(request.POST)
		if data.is_valid():
			data.save()
			msg="student add sucessfully"

			return render(request,"createStudent.html",{"message":msg,"form":form_obj_varble})
		else:
			msg="Check Error"
			return render(request,"createStudent.html",{"message":msg,"form":form_obj_varble})

	else:
		return render(request,"createStudent.html",{"form":form_obj_varble})


def view_student(request):
	data=StudentModel.objects.all()
	return render(request,"viewStudent.html",{"received_data":data})
	


def delete_student(request,rno):
	data=get_object_or_404(StudentModel,rollno=rno)
	if request.method=="POST":
		data.delete()
		return redirect("view_stdn")
	else:
		return render(request,"deleteStudent.html",{"received_data":data})

		
	




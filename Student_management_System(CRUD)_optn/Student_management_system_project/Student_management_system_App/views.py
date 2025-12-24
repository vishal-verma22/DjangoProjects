from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import StudentModel

# Create your views here.

def create(request):
	if request.method=="POST":
		forms_obj_varble=StudentForm(request.POST)
		if forms_obj_varble.is_valid():
			forms_obj_varble.save()
			msg="Student Created Successfully"
			return render(request,"create.html",{"form":forms_obj_varble,"message":msg})
		else:
			msg="check Error"
			return render(request,"create.html",{"form":forms_obj_varble,"message":msg})

	else:
		forms_obj_varble=StudentForm()
		return render(request,"create.html",{"form":forms_obj_varble})
	
def ViewStudentInfo(request):
	data=StudentModel.objects.all()
	return render(request,"view_stdtn_data.html",{"Recived_data":data})


# for delete we have 2 way without using get_object_or_404  or with using get_object_or_404 

#without using get_object_or_404 

'''def delete(request,rno):
	try:
		data=StudentModel.objects.get(rollno=rno)

		if request.method=="POST":
			data.delete()
			return redirect('/')  # ← sahi tarika
		else:
			return render(request,"delete.html",{"rollno":rno})
	except StudentModel.DoesNotExist:
		return redirect('/')'''

#with using get_object_or_404 

def delete(request,rno):
	data=get_object_or_404(StudentModel,rollno=rno)
	if request.method=="POST":
		data.delete()
		return redirect("/")	
	else:
		return render(request,"delete.html",{"received_data":data})	
def update(request,rno):
	data=get_object_or_404(StudentModel,rollno=rno)

	if request.method=="POST":
		data=StudentForm(request.POST,instance=data)
		data.save()
		return redirect("/")
	else:	
		form_obj_with_data=StudentForm(instance=data)
		form_obj_with_data.fields["rollno"].widget.attrs['readonly']=True
		return render(request,"update.html",{"form":form_obj_with_data})



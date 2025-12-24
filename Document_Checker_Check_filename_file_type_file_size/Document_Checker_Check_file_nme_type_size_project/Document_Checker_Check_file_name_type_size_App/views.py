from django.shortcuts import render
from .forms import DocumentForm

# Create your views here.

def DocumentFormat_checker(request):
	form_obj_variable=DocumentForm()
	if request.method=="POST":
		name=request.POST.get("name")
		rollno=request.POST.get("Rollno")
		marksheet=request.FILES.get("marksheet")
		IdCard=request.FILES.get("Id_Card")

		error_msg=[]

		for filed_Name,file_object in [("marksheet",marksheet),("Id_Card",IdCard)]:
			if not file_object:
        			continue 

			Name=file_object.name
			Size=file_object.size		
			extension=Name.split(".")[-1].lower()
			
		 
			#Checking space in file name
			if " " in Name:
				error_msg.append(f"{Name} : Spaces are not allowed")
						#Checking correct (Extension) file type
			if not extension in ["jpg","pdf", "docx", "txt"] :
				error_msg.append(f"{Name} : has invalid file type")
						#checking file size
			max_size=8*1024*1024  # 8 mb is max(8*1024kb*1024*bytes)
			if Size>max_size:
				error_msg.append(f"{Name} : size exceeds 8MB")
		success_msg=f"Name :{name}<br> Rollno:{rollno}<br> Your Document uploaded successfully"	
		return render(request,"home.html",{"Error":error_msg,"Success":success_msg,"form":form_obj_variable})
	else:
		return render(request,"home.html",{"form":form_obj_variable})

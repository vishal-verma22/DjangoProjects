from django.contrib import admin
from django.urls import path
from Student_management_system_App.views import ViewStudentInfo,create,delete,update
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ViewStudentInfo,name="home"),
    path("createpage",create,name="create"),
    path("deletepage/<int:rno>",delete,name="delete"),
    path("updatepage/<int:rno>",update,name="update")
]

"""
URL configuration for Collage_management_Sys_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Collage_management_Sys_App.views import home,create_dept,view_dept,delete_dept,Create_student,view_student,delete_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path("add_department",create_dept,name="add_dept"),
    path("view_department",view_dept,name="view_dept"),
    path("delete_department/<int:id>",delete_dept,name="delete_dept"),
    path("add_student",Create_student,name="add_stdn"),
    path("view_student",view_student,name="view_stdn"),
    path("delete_student/<int:rno>",delete_student,name="delete_stdn"),



]

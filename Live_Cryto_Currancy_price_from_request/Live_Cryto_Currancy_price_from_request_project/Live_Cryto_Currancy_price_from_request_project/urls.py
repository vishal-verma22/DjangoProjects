from django.contrib import admin
from django.urls import path
from Live_Cryto_Currancy_price_from_request_App.views import get_Live_price
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',get_Live_price),
   
]

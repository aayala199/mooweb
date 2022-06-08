from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    
    path('',views.alquiler, name="alquiler"),
    path('test/',views.test, name="test"),
   
    #re_path(r'^.*\.*', views.pages, name='pages'), #match any page
    
]
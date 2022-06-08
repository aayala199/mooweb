from django.urls import path
from moobecweb import views

urlpatterns = [
    path('',views.home, name="home"),
    #path('alquiler',views.alquiler , name="alquiler"),
    #path('empresas',views.empresas, name="empresas"),
    path('contacto',views.contacto, name="contacto"),
    path('404', views.error_page, name="error"),
]
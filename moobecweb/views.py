from django.shortcuts import render
from servicios.models import Servicios

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def alquiler(request):
    return render(request,"home/alquiler.html")


def contacto(request):
    return render(request,"home/contacto.html")

def error_page(request):
    return render(request,"home/404.html")

from django.shortcuts import render
from servicios.models import Servicios

# Create your views here.

def empresas(request):
    servicios=Servicios.objects.all() #importar todos los campos de la clase Servicios
    return render(request,"servicios/empresas.html", {"servicios": servicios })


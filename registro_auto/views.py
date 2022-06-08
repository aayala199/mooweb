from django.shortcuts import render
from .forms import FormularioRegistroAuto
from .forms2 import unirmeForm
from django.http import HttpResponseRedirect


# Create your views here.
"""def alquiler(request):
    formularioregistroauto= FormularioRegistroAuto()
    unirme= unirmeForm()
    return render(request,"home/alquiler.html", {'formulario': formularioregistroauto, 'unirme': unirme})
"""
def alquiler(request):
    submitted= False
    if request.method == "POST":
        unirme= unirmeForm(request.POST)
        if unirme.is_valid():
            unirme.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        unirme= unirmeForm
        if 'submitted' in request.GET:
            submitted= True
    return render(request, 'home/alquiler.html', {'unirme': unirme, 'submitted': submitted})

def test(request):
    submitted= False
    if request.method == "POST":
        unirme= unirmeForm(request.POST)
        if unirme.is_valid():
            unirme.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        unirme= unirmeForm
        if 'submitted' in request.GET:
            submitted= True
    return render(request, 'home/test.html', {'unirme': unirme, 'submitted': submitted})
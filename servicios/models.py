from operator import truediv
from django.db import models

# Create your models here.

class Servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    icono=models.CharField(max_length=20, default='n/a')
    #imagen=models.ImageField()
    creado =models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"

    def __str__(self):
        return self.titulo
import email
from django.db import models
from django.forms import CharField

# Create your models here.

class RegistroAuto(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=12)
    modelo = models.CharField(max_length=12)
    year = models.IntegerField()
    vin = models.CharField(max_length=17)
    millas = models.IntegerField()
    categoria = models.IntegerField()
    locacion = models.IntegerField()
    disponibilidad = models.BooleanField()
    creado =models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Registrar auto"
        verbose_name_plural="Registrar autos"

    def __str__(self):
        return self.placa


yearChoises=[tuple([x,x]) for x in range(2016,2024)]

kmChoises=[
    ('0-15000', '0-15000 km'),
    ('15-50000', '15-50000 km'),
    ('50-100000', '50-100000 km'),
    ('100-150000', '100-150000 km'),
    ('+150000', '+150000 km'),
]
locacionChoises=[
    ('guayaquil', 'Guayaquil'),
    ('quito', 'Quito'),
    ('cuenca', 'Cuenca'),
]

estadoChoices=[
    ('contactado','Contactado'),
    ('registroauto','Registro auto'),
    ('noInteresado','No esta interesado')
]


class unirmeRegistro(models.Model):
    marca = models.CharField(max_length=12)
    modelo = models.CharField(max_length=12)
    year = models.IntegerField()
    millas = models.CharField(max_length=20)
    locacion = models.CharField(max_length=25)
    nombre=models.CharField(max_length=100)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)
    #Contactado = models.BooleanField(default=0)
    estado=models.CharField(choices=estadoChoices, max_length=30, default='n/a')
    comentario=models.TextField(null=True, blank=True)
    creado =models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Solicitud web"
        verbose_name_plural="Solicitud web"


    def __str__(self):
        return self.marca


from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=50)
    creado =models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.titulo

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    #imagen=models.ImageField(upload_to="blog", null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    creado =models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Pxsost"
        verbose_name_plural="Posts"

    def __str__(self):
        return self.titulo
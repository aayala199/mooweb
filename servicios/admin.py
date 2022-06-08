from django.contrib import admin
from .models import Servicios
# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')
    list_display=('titulo', 'contenido')
    search_fields=('titulo',)


admin.site.register(Servicios, ServiciosAdmin)

from django.contrib import admin
from .models import RegistroAuto, unirmeRegistro

# Register your models here.
class RegistroAutoAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')
    list_display=('placa','marca', 'modelo', 'year', 'disponibilidad', 'locacion')#campos a mostar como tablas
    search_fields=('placa',)#siempre coma al final si es solo un campo como parametro de busqueda
    

class unirmeAdmin(admin.ModelAdmin):
    readonly_fields=('creado','actualizado')
    list_display=('nombre','marca', 'modelo', 'year', 'locacion', 'email', 'telefono', 'estado')
    search_fields=('telefono', 'email', 'nombre')

admin.site.register(RegistroAuto, RegistroAutoAdmin)
admin.site.register(unirmeRegistro, unirmeAdmin)
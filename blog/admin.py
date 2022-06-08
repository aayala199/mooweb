from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')
    list_display=('titulo',)
    search_fields=('titulo',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')
    list_display=('titulo','contenido', 'autor')
    search_fields=('titulo','autor', 'categoria')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
from django.contrib import admin

from .models import CategoriaProd, Productos

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(CategoriaProd, CategoriaAdmin)
admin.site.register(Productos, ProductosAdmin)
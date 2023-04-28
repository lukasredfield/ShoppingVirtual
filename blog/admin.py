from .models import Categoria, Post
from django.contrib import admin

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

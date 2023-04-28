from django.db import models
from django.contrib.auth. models import User

# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=50) 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo=models.CharField(max_length=50) 
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    #Vamos a crear una propiedad "autor" para que cada entrada de blog que realice un autor determinado, al momento de retirarse la página, todos sus blogs sean borradas.
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #Ahora vamos a crear esta propiedad que nos indica que un blog puede pertenecer a varias categorias.
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo

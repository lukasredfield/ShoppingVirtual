from email.policy import default
from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50) 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoriaProd'
        verbose_name_plural='categoriasProd'

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre=models.CharField(max_length=50,null=True) 
    precio=models.IntegerField(null=True)
    stock=models.IntegerField(null=True)
    imagen=models.ImageField(upload_to='tienda', null=True, blank=True)
    #Vamos a crear una propiedad "autor" para que cada entrada de blog que realice un autor determinado, al momento de retirarse la página, todos sus blogs sean borradas.
    #autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #Ahora vamos a crear esta propiedad que nos indica que un blog puede pertenecer a varias categorias.
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def __str__(self):
        return self.nombre

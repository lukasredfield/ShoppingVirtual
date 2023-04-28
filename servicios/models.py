from email.headerregistry import ContentDispositionHeader
from tabnanny import verbose
from django.db import models

# Create your models here.

""" Ahora dentro de este servicio vamos a crear una base de datos.
para ello vamos a crear una clase. Esta clase va a convertirse en la tabla de la base de
datos que vamos a utilizar. Esta funcionalidad de Django se llama "Mapeo ORM" o "Mapeo de Objetos Relacional".
Cada atributo de la clase va a corresponder a un campo de la tabla de la base de datos, o en este caso,
de cada servicio de nuestra web. El Mapeo ORM consiste en crear un objeto de clase y ese objeto va a representar
un objeto o elemento de la tabla con sus propiedades.
"""

class Servicio(models.Model):
    titulo=models.CharField(max_length=50) 
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo

"""Esta clase "Modelo" tiene una serie de caracteristicas. Estas caracteristicas se llaman "meta".
Las Opciones Meta de Modelos son metodos especiales aplicables a las caracteristicas del modelo.
Para ello hay que crear dentro de la clase otra clase:  """

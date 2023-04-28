from django.contrib import admin
from .models import Servicio

# Register your models here.

"""Ahora vamos a configurar nuestro panel de control para poder ver y manipular
nuestra base de datos desde la administración de nuestra web.
Para ello primero tenemos que registrar nuestra nueva aplicación "servicios" en el
archivo "settings" de nuestro proyecto, en el apartado de "INSTALLED_APPS".
Luego vamos importar del archivo "models" la clase del servicio de nuestra base de datos.
de la siguiente manera "from .models import Servicio" (poniendole un punto al principio
porque estas accediendo a una instancia o modulo en que ya se escuentra este archivo "admin",
los dos estan en el mismo lugar)
Luego vamos a registrar el modelo o "clase" de nuestra base de datos en nuestro archivo admin.
 con la siguiente instrucción: admin.site.register(Servicio)
 Luego de esto en nuestro panel de administración vamos a poder insertar y modificar nuestra
 tabla de base de datos. Y si queremos ver los demás campos de nuestra base de datos
 vamos a crear una clase que herede en los parametros el admin.ModelAdmin y abajo 
 vamos a poner que busque las propiedades de la tabla que no se pueden modificar como es el 
 caso nuestro (porque se autocompletan) Para ellos vamos a referenciar estas propiedades con:
 una variable de tipo "readonly_fields". """

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio, ServicioAdmin)



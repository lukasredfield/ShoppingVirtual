from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.blog, name="Blog"),
    path('categorias/<int:categoria_id>/', views.categorias, name="categoriaa"),

#Dentro del "name" que contiene como valor "categoriaa", esta haciendo referencia
#a la clave con la cual vamos a llamar al path desde la hoja de html en la sección de filtrado de 
#categorias de entradas de blog.
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
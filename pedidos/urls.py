from pedidos.views import procesar_pedidos
from tienda.views import tienda
from django.urls import path

urlpatterns = [
    path('procesar_pedidos/', procesar_pedidos, name='procesar_pedidos'),
    path('tienda/', tienda, name='Tienda'),
]


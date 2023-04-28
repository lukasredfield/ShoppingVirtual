from django.urls import path

from . import views

urlpatterns = [
    
    path('tienda', views.tienda, name="Tienda"),
    path('comprahecha', views.comprar, name="Comprahecha"),
    path('categorias/<int:categoria_id>/', views.categorias, name="categoria2"),
    
]

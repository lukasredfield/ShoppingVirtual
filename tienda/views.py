from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Productos, CategoriaProd

# Create your views here.

from carro.carro import Carro

def tienda(request):
    produ = Productos.objects.all()
    carro = Carro(request)
    importe_total_carro = carro.precio_total()

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        producto = Productos.objects.get(id=producto_id)
        carro.agregar(producto)
        messages.success(request, 'El producto se ha añadido al carrito con éxito.')
        return redirect('tienda')

    return render(request, './Tienda.html', {"produs": produ, "importe_total_carro": importe_total_carro})
#El ultimo parámetro del render() "{"posteos": posts}" es una forma de llamar a la base de datos.
#Es una Queryset. Al parecer un Queryset es una especie de diccionario con una colección de tods los objetos
#de la base de datos. Y se la llama con un nombre de variable, en este caso "posteos" dos puntos y el nombre 
#de la variable que creamos arriba que contiene todos los objetos osea "post" (posts=Post.objects.all())

def categorias(request, categoria_id):

    categoria2=CategoriaProd.objects.get(id=categoria_id)
    produ=Productos.objects.filter(categorias=categoria2)
    return render(request, "tienda/categoria.html",{'categoria2':categoria2,"produs": produ})

def comprar(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return render(request, "./comprahecha.html")




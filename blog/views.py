from django.shortcuts import render
from blog.models import Post, Categoria


# Create your views here.

def blog(request):

    posts=Post.objects.all()
    return render(request, 'blog/Blog.html', {"posteos": posts})

#El ultimo parámetro del render() "{"posteos": posts}" es una forma de llamar a la base de datos.
#Es una Queryset. Al parecer un Queryset es una especie de diccionario con una colección de tods los objetos
#de la base de datos. Y se la llama con un nombre de variable, en este caso "posteos" dos puntos y el nombre 
#de la variable que creamos arriba que contiene todos los objetos osea "post" (posts=Post.objects.all())

def categorias(request, categoria_id):

    categoria1=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria1)
    return render(request, "blog/categorias.html",{'categoria1':categoria1,"posts": posts})


    
from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, 'ProyectoWebApp/Home.html')

def home2(request):

    return render(request, 'ProyectoWebApp/Home2.html')

def informacion(request):

    return render(request, 'ProyectoWebApp/Información.html')

# def tienda(request):

#     return render(request, 'ProyectoWebApp/Tienda.html')









from django.shortcuts import redirect, render

"""Metodo 1 para envíar e-mails"""

from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.

def contacto(request): 

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

        #Ahora vamos a enviar el mail con la información del formulario:
        #Para ellos vamos a importar la clase "EmailMessage". Luego vamos a crear 
        #Un objeto de tipo EmailMessage y vamos a completar los parametros que nos solicita
        #esta clase determinada:
        #- Asunto
        #- Cuerpo del mensaje
        #- La dirección de quien envía este mail (osea Django con el mail que le pusimos en settings)
        #- La cuenta con la que queremos contactar
        #- 

            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),"",["lukasredfield@gmail.com"],reply_to=[email])

        try:
            email.send()

            return redirect("./?valido")
        except:
            return redirect("./?novalido")


    return render(request, './Contacto.html',{'mi_formulario':formulario_contacto})
from django.shortcuts import render

"""Metodo 2 para envíar e-mails"""

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

# Create your views here.

def envia_email(mail):
    context = {'mail':mail}

    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba','Codigofacilito', settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()


def sendmail(request):

    if request.method == 'POST':
        mail = request.POST.get('mail')
        envia_email(mail)

    return render(request, './sendmail.html', {})



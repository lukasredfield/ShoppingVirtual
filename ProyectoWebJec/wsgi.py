import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoWebJec.settings')

#application = get_wsgi_application()

"""Nuevas variables agregadas"""

from dj_static import Cling

application = Cling(get_wsgi_application())


from django.urls import path

from ProyectoWebJecApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    #path('home2', views.home2, name="Home2"),
    #path('tienda', views.tienda, name="Tienda"),
    #path('sendmail', views.tienda, name="sendmail"),


]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

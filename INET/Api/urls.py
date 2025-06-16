from django.urls import path,include    
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('logouts/', salir, name='logouts'),
    path('Registro/', Registro, name='registro'),
    path('Administrador/', AgregarPaquete, name='Admin'),
]
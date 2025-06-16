from django.urls import path,include    
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('logout/', salir, name='logout'),
    path('Registro/', Registro, name='registro'),
]
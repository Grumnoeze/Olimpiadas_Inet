from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 

from .models import *
from .forms import *

from django.db.models import Q

from django.contrib.auth import logout,login,authenticate

from django.contrib.admin.views.decorators import staff_member_required

def Home(request):
    query= Paquete.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            query = Paquete.objects.filter(
                Q(nombre__icontains=search) | 
                Q(descripcion__icontains=search)
            )
    else:
        query = Paquete.objects.all()
    return render (request,"Index.html")

def salir(request):
    logout(request)
    return redirect('home')

def Registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    query = CustomUserCreationForm(data=request.POST)
    if query.is_valid():
        query.save()
        user=authenticate(username=query.cleaned_data['username'],
                          password=query.cleaned_data['password1'])
        login(request,user)
        return redirect('home')
    data['form'] = query
    return render(request, 'registration/registro.html', data)

# Create your views here.

staff_member_required(login_url='login')
def AgregarPaquete(request):
    data = {
        'forms': AddPaquete()
    }
    if request.method == 'POST':
        formulario = AddPaquete(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
        else:
            data['forms'] = formulario
    return render(request, 'pages/administrador.html', data)

# def vistapaquetes(request):
#     paquetes = Paquete.objects.all()
#     data = {
#         'paquetes': paquetes
#     }
#     return render(request, 'pages/packages.html', data)
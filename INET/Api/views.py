from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 

from .models import *
from .forms import *

from django.db.models import Q

from django.contrib.auth import logout,login,authenticate

def Home(request):
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


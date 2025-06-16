from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    pass


class AddPaquete(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = "__all__"
        widgets = {
            'fecha_vuelo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_regreso': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_vuelo = cleaned_data.get("fecha_vuelo")
        fecha_regreso = cleaned_data.get("fecha_regreso")
        
        if fecha_regreso and fecha_vuelo and fecha_regreso < fecha_vuelo:
            raise forms.ValidationError("La fecha de regreso no puede ser anterior a la fecha de vuelo.")
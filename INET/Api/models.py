from django.db import models
from django.forms import ValidationError




# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=16)

    def __int__(self):
        return self.nombre

class Paquete(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio_uni = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vuelo = models.DateField(null=True, blank=True)
    fecha_regreso = models.DateField(null=True, blank=True)
    
    def clean(self):
            if self.fecha_regreso < self.fecha_vuelo:
                raise ValidationError("La fecha de regreso no puede ser anterior a la fecha de vuelo.")
    def __int__(self):
        return self.nombre
    

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.paquete.precio_unit * self.cantidad
        super().save(*args, **kwargs)
    def __int__(self):
        return self.usuario.nombre
    
class Aplicacion(models.Model):
    def __int__(self):
        return self.nombre


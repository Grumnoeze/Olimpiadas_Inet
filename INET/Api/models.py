from django.db import models

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
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    def __int__(self):
        return self.nombre
    

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.usuario.nombre
    
class Aplicacion(models.Model):
    

    def __int__(self):
        return self.nombre


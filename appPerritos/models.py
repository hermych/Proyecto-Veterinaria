from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(default = 'null')
    registrado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

class Raza(models.Model):
    nombre = models.CharField(max_length=110)
    descripcion = models.CharField(max_length=250)
    creado = models.DateField()
from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)
    correo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre + " " + self.apellidos

class Sitio(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


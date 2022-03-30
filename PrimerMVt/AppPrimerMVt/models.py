from pyexpat import model
from django.db import models

# Create your models here.
class Familiares(models.Model):
    idFamiliar = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=60)
    fechaNacimiento = models.DateField()

    def __str__(self):
        txt = "Nombre: {0} Apellido: {1} Fecha Nacimiento: {2}"
        return txt.format(self.nombre,self.apellidos,self.fechaNacimiento)

class Parentesco(models.Model):
    idParentesco = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=30)

    def __str__(self):
        txt = "Parentesco: {0}"
        return txt.format(self.parentesco)

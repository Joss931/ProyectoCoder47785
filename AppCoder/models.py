from django.db import models

# Create your models here.
class Curso(models.Model): # crea una herecia
    nombre = models.CharField(max_length=40) # cantidad maxima
    camada = models.IntegerField(max_length=40)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    emaio = models.EmailField()
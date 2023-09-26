from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=200)

class tareas(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(project, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=20)
    correo = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
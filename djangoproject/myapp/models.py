from django.db import models

# Create your models here.

diurno = "[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]"
vespertino = "[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]"

class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__ (self):
        return self.name

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    proyecto = models.ForeignKey(Project, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=255)
    rut = models.CharField(max_length=20)
    correo = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)

    def __str__ (self):
        return self.name

class Profesor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)
    jornada = models.CharField(max_length=45)
    diurno = models.CharField(max_length=250, default=diurno)
    vespertino = models.CharField(max_length=250, default=vespertino)

class SecretarioAcademico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Carrera = models.CharField(max_length=255)

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


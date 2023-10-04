from django.db import models

# Create your models here.

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

class Profesor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Horario(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    matriz = models.CharField(max_length=250, default='default_value')

class SecretarioAcademico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Carrera = models.CharField(max_length=255)

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


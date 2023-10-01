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

class Day(models.Model):
    name = models.CharField(max_length=10)

class Hour(models.Model):
    time = models.TimeField()

class Horario(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE)
    modalidad = models.CharField(max_length=20)
    Disponibilidad = models.BooleanField(default=False)

class SecretarioAcademico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Carrera = models.CharField(max_length=255)

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
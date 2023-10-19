from django.db import models

# Create your models here.

diurno = "[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]"
vespertino = "[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]"

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

    def __str__ (self):
        return self.name

class Auditoria(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    evento = models.CharField(max_length=255)
    fechaHora = models.CharField(max_length=255)

class Profesor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)
    jornada = models.CharField(max_length=45)
    horarioDiurno = models.CharField(max_length=250, default=diurno)
    horarioVespertino = models.CharField(max_length=250, default=vespertino)

class SecretarioAcademico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Carrera = models.CharField(max_length=255)

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PlanificacionAcademica(models.Model):
    programa = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    jornada = models.CharField(max_length=255)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

class Curso(models.Model):
    planificacionAcademica = models.ForeignKey(PlanificacionAcademica, on_delete=models.CASCADE)
    facultad = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    unidadAcademica = models.CharField(max_length=255)
    periodo = models.CharField(max_length=255)
    materia = models.CharField(max_length=255)
    Curso = models.CharField(max_length=255)
    seccion = models.CharField(max_length=10)
    jornada = models.CharField(max_length=20)
    nrc = models.CharField(max_length=20)
    listaCruzada = models.CharField(max_length=255)
    nrcLigados = models.CharField(max_length=255)
    idListaCurzada = models.IntegerField()
    calificable = models.IntegerField()
    minor = models.IntegerField()
    nombreAsignatura = models.CharField(max_length=255)
    horasAPagar = models.IntegerField()
    tipoActividad = models.CharField(max_length=255)
    modalidad = models.CharField(max_length=20)
    numeroVacantes = models.IntegerField()
    numeroInscritos = models.IntegerField()
    restriccionCodPrograma = models.CharField(max_length=255)
    restriccionDescPrograma = models.CharField(max_length=255)
    restriccionCampus = models.CharField(max_length=255)
    nivelCurso = models.IntegerField()
    unidadQuePaga = models.CharField(max_length=255)
    semestreQuePaga = models.CharField(max_length=20)
    prorcentajeOnline = models.FloatField()
    proveedor = models.CharField(max_length=255)
    administrador = models.CharField(max_length=255)
    iniciativa = models.CharField(max_length=255)
    aulas = models.CharField(max_length=255)

class HorarioCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    horaInicio = models.CharField(max_length=255)
    horaFin = models.CharField(max_length=255)
    dia = models.CharField(max_length=255)

class ProfesorCurso(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

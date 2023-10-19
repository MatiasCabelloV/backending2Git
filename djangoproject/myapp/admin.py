from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tarea)
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Profesor)
admin.site.register(SecretarioAcademico)
admin.site.register(Admin)
admin.site.register(Auditoria)
admin.site.register(PlanificacionAcademica)
admin.site.register(Curso)
admin.site.register(HorarioCurso)
admin.site.register(ProfesorCurso)
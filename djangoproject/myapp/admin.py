from django.contrib import admin
from .models import Tarea, Project, User, Profesor,SecretarioAcademico, Admin
# Register your models here.

admin.site.register(Tarea)
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Profesor)
admin.site.register(SecretarioAcademico)
admin.site.register(Admin)
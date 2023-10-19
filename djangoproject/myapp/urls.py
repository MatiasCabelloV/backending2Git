from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'project', views.ProjectSeri, 'Project')
router.register(r'tarea', views.TareaSeri, 'Tarea')
router.register(r'user', views.UserSeri, 'User')
router.register(r'profesor', views.ProfesorSeri, 'Profesor')
router.register(r'secretario-academico', views.SecretarioAcademicoSeri, 'SecretarioAcademico')
router.register(r'admin', views.AdminSeri, 'Admin')
router.register(r'planificacion-academica', views.PlanificacionSeri, 'PlanificacionAcademica')
router.register(r'curso', views.CursoSeri, 'Curso')
router.register(r'horario-curso', views.HorarioSeri, 'HorarioCurso')
router.register(r'profesor-curso', views.ProfesorCursoSeri, 'ProfesorCurso')
router.register(r'auditoria', views.AuditoriaSeri, 'Auditoria')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('profesor/', views.profesor, name='v_profesor'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('signin/', views.iniciar_sesion, name='iniciar_sesion')
]

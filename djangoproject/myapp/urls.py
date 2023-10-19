from django.urls import path, include
from rest_framework import routers
from . import views

router1 = routers.DefaultRouter()
router1.register(r'myapp', views.ProjectSeri, 'Project')

router2 = routers.DefaultRouter()
router2.register(r'myapp', views.TareaSeri, 'Tarea')

router3 = routers.DefaultRouter()
router3.register(r'myapp', views.UserSeri, 'User')

router4 = routers.DefaultRouter()
router4.register(r'myapp', views.ProfesorSeri, 'Profesor')

router5 = routers.DefaultRouter()
router5.register(r'myapp', views.SecretarioAcademicoSeri, 'SecretarioAcademico')

router6 = routers.DefaultRouter()
router6.register(r'myapp', views.AdminSeri, 'Admin')

router7 = routers.DefaultRouter()
router7.register(r'myapp', views.PlanificacionSeri, 'PlanificacionAcademica')

router8 = routers.DefaultRouter()
router8.register(r'myapp', views.CursoSeri, 'Curso')

router9 = routers.DefaultRouter()
router9.register(r'myapp', views.HorarioSeri, 'HorarioCurso')

router10 = routers.DefaultRouter()
router10.register(r'myapp', views.ProfesorCursoSeri, 'ProfesorCurso')

router11 = routers.DefaultRouter()
router11.register(r'myapp', views.AuditoriaSeri, 'Auditoria')

urlpatterns = [
    path('api/v1/', include(router1.urls)),
    path('api/v2/', include(router2.urls)),
    path('api/v3/', include(router3.urls)),
    path('api/v4/', include(router4.urls)),
    path('api/v5/', include(router5.urls)),
    path('api/v6/', include(router6.urls)),
    path('api/v7/', include(router7.urls)),
    path('api/v8/', include(router8.urls)),
    path('api/v9/', include(router9.urls)),
    path('api/v10/', include(router10.urls)),
    path('api/v11/', include(router11.urls)),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('profesor/', views.profesor, name='v_profesor'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('signin/', views.iniciar_sesion, name='iniciar_sesion')
]

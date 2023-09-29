from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('profesor/', views.profesor, name='v_profesor'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('signin/', views.iniciar_sesion, name='iniciar_sesion')
]

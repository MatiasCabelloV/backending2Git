from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import horario
#from django.contrib.auth.decorators import de
from rest_framework import viewsets
from .serializer import *
from .models import *

# VISTA JSX
class ProjectSeri(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TareaSeri(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()

class UserSeri(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfesorSeri(viewsets.ModelViewSet):
    serializer_class = ProfesorSerializer
    queryset = Profesor.objects.all()

class SecretarioAcademicoSeri(viewsets.ModelViewSet):
    serializer_class = SecretarioAcademicoSerializer
    queryset = SecretarioAcademico.objects.all()

class AdminSeri(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()

class PlanificacionSeri(viewsets.ModelViewSet):
    serializer_class = PlanificacionSerializer
    queryset = PlanificacionAcademica.objects.all()

class CursoSeri(viewsets.ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()

class HorarioSeri(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    queryset = HorarioCurso.objects.all()

class ProfesorCursoSeri(viewsets.ModelViewSet):
    serializer_class = ProfesorCursoSerializer
    queryset = ProfesorCurso.objects.all()

class AuditoriaSeri(viewsets.ModelViewSet):
    serializer_class = AuditoriaSerializer
    queryset = Auditoria.objects.all()

# VISTA TEMPLATES
def home(request):
    return render(request, 'home.html')

def registro(request):
    
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                                                password=request.POST['password1'])
                user.save()
                login(request, user) #PAra agregar la cookie del inicio de sesion y saber que usuario es y sus permisos
                return redirect('v_profesor')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Contraseñas no coinciden'
        })

def profesor(request):
    return render(request, 'v_profesor.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {
        'form': AuthenticationForm
        })
    else:
        print(request.POST)
        
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'inicio_sesion.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('v_profesor')
        
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
#from django.contrib.auth.decorators import de

# Create your views here.
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
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Contraseñas no coinciden'
        })

def tareas(request):
    return render(request, 'tarea.html') 

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
            return redirect('tareas')
        
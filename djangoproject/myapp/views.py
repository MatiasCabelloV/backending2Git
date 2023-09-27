from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
#from django.contrib.auth.decorators import de

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], 
                                                password=request.POST['password1'])
                user.save()
                return HttpResponse('Registro exitoso')
            except:
                return HttpResponse('Usuario ya existe')
        return HttpResponse('Contraseñas no coinciden')
    

@login_required
def account(request):
    return render(request, 'account.html')
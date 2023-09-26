from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import de

# Create your views here.
def home(request):
    return HttpResponse("Has iniciado sesion")

def about(request):
    return HttpResponse("About")

def login(request):
    return HttpResponse("login")

def logout(request):
    return redirect('login')
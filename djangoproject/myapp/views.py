from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About")

def login(request, correo, password):
    return HttpResponse("login")
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import de

# Create your views here.
def index(request):
    print(request)
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About")

def logout(request):
    return redirect('index.html')
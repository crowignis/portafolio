from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def inicio(request):
    return render(request, 'app/inicio.html')

def registro1(request):
    return render(request, 'app/registro1.html')


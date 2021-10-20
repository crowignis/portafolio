
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProveedorForm


# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def inicio(request):
    return render(request, 'app/inicio.html')

def registro1(request):
    return render(request, 'app/registro1.html')

def proveedor_view(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else: 
        form = ProveedorForm()
   
    return render(request,'app/proveedor.html', {'form':form})


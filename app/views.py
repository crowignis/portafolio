
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductoForm, ProveedorForm, RecetaForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.


def home(request):
    return render(request, 'app/home.html')


@permission_required('app.add_producto')
def productoView(request):

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto registrado correctamente")
            return redirect('home')
    else: 
        
        form = ProductoForm()

    
    return render(request, 'app/producto.html', {'form': form})

@permission_required('app.add_proveedor')
def proveedor_view(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Proveedor registrado correctamente")
            return redirect('home')
    else: 
        form = ProveedorForm()
   
    return render(request,'app/proveedor.html', {'form': form})

@permission_required('app.add_receta')
def recetaView(request):

    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Receta registrada correctamente")
            return redirect('home')
        
    else: 
        
        form = RecetaForm()

    
    return render(request, 'app/receta.html', {'form': form})


def registro(request):
    data = {
        'form': CustomUserCreationForm()
        
    }
    
    if request.method == 'POST': 
        formulario = CustomUserCreationForm(data=request.POST)
        data["form"] = formulario
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Usuario registrado correctamente")
            return redirect(to="home")
        
      
        




    return render(request, 'registration/registro.html', data)
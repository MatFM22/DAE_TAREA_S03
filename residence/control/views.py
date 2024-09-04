from django.shortcuts import render, redirect
from .forms import PropietarioForm, VehiculoForm, RegistroForm
from .models import Propietario, Vehiculo, Registro

# Create your views here.

def index(request):
    return render(request, 'control/index.html')

def registrar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control:index')  
    else:
        form = PropietarioForm()
    return render(request, 'control/registrar_propietario.html', {'form': form})

def registrar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control:index')  
    else:
        form = VehiculoForm()
    return render(request, 'control/registrar_vehiculo.html', {'form': form})

def registrar_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('control:index') 
    else:
        form = RegistroForm()
    return render(request, 'control/registrar_registro.html', {'form': form})

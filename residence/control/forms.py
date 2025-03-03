from django import forms
from .models import Propietario, Vehiculo, Registro

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'numero_apartamento', 'telefono', 'email']

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['propietario', 'matricula', 'marca', 'modelo', 'color']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['vehiculo', 'fecha_hora_entrada', 'fecha_hora_salida']
        
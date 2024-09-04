from django.urls import path
from . import views

app_name = 'control'

urlpatterns = [
    path('', views.index,name='index'),
    path('propietario/', views.registrar_propietario, name='registrar_propietario'),
    path('vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('registro/', views.registrar_registro, name='registrar_registro'),
]
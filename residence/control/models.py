from django.db import models

# Create your models here.
class Propietario(models.Model):
    nombre=models.CharField(max_length=30)
    numero_apartamento=models.IntegerField()
    telefono=models.CharField(max_length=15)
    email=models.EmailField()

    def __str__(self):
        return self.nombre
    
class Vehiculo(models.Model):
    propietario=models.ForeignKey(Propietario, on_delete=models.CASCADE)
    matricula=models.CharField(max_length=8, unique=True)
    marca=models.CharField(max_length=15)
    modelo=models.CharField(max_length=20)
    color=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.marca} - {self.matricula}'

class Registro(models.Model):
    vehiculo=models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora_entrada=models.DateTimeField()
    fecha_hora_salida=models.DateTimeField(null=True, blank=True)

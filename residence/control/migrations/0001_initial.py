# Generated by Django 5.1.1 on 2024-09-04 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('numero_apartamento', models.IntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=8, unique=True)),
                ('marca', models.CharField(max_length=15)),
                ('modelo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora_entrada', models.DateTimeField()),
                ('fecha_hora_salida', models.DateTimeField(blank=True, null=True)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.vehiculo')),
            ],
        ),
    ]

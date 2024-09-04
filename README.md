Descargar el proyecto "Residence", este va almacener la la aplicación "control" en la que vamso a poder encontrar los Módulos, Forms, Plantillas y Diseños.
Si presenta error con el diseño, dirigase al archivo settings.py del proyeto residence, y configurar lo siguiente: STATIC_URL = '/static/'
Después de eso volver a ejecutar el comando "python manage.py runserver", por si los cambios no se aplicaron.

Si en la terminal se presenta el error "database is locked", cerrar la base de datos y volver a abrir el proyecto.

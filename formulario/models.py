from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class DatosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    AñoGraduacion = models.IntegerField()# Relación con el usuario  
    sede = models.CharField(max_length=50, choices=[
        ('Medellín', 'Medellín'),
        ('Pereira', 'Pereira'),
        ('Rionegro', 'Centro tutorial Rionegro'),
        ('Apartado', 'Centro tutorial Apartado'),
    ])
    
    programa = models.CharField(max_length=100, choices=[
        ('Administración de empresas', 'Administración de empresas'),
        ('Administración de Mercadeo', 'Administración de Mercadeo'),
        ('Administración de negocios Internacionales', 'Administración de negocios Internacionales'),
        ('Administración Turística y Hotelera', 'Administración Turística y Hotelera'),
        ('Derecho', 'Derecho'),
        ('Especialización en Gerencia de Mercadeo', 'Especialización en Gerencia de Mercadeo'),
        ('Especialización en gerencia del talento Humano', 'Especialización en gerencia del talento Humano'),
        ('Especialización de Sanidad Animal', 'Especialización de Sanidad Animal'),
        ('Ingeniería Administrativa', 'Ingeniería Administrativa'),
        ('Ingeniería de software', 'Ingeniería de software'),
        ('Medicina', 'Medicina'),
    ])
    NombreCompleto = models.CharField(max_length=200)  
    cedula = models.CharField(max_length=20)
    genero = models.CharField(max_length=10, choices=[
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro'),
    ])
    
    celular = models.CharField(max_length=20)
    correo = models.EmailField()
    pais = CountryField(blank_label='Seleccione un país')
    ciudad = models.CharField(max_length=100, blank=True)
    TemasEventos = models.CharField(max_length=10, choices=[
        ('Cursos', 'Cursos'),
        ('Diplomados', 'Diplomados'),
        ('Talleres', 'Talleres'),
    ])
    AreasBienestar = models.CharField(max_length=50, choices=[
        ('Deporte', 'Deporte'),
        ('Recreación', 'Recreación'),
        ('Cultura', 'Cultura'),
        ('Salud', 'Salud'),
        ('Desarrollo Humano', 'Desarrollo Humano'),
        ('Promoción Socioeconómica', 'Promoción Socioeconómica'),
    ])
    OtrasActividades = models.TextField()
    observaciones = models.TextField(blank=True)


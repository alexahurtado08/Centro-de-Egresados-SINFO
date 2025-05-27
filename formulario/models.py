from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone



class DatosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    AñoGraduacion = models.IntegerField()# Relación con el usuario  
    
    sede = models.CharField(max_length=100, choices=[
        ('Medellín', 'Medellín'),
        ('Pereira', 'Pereira'),
        ('Centro Tutorial Rionegro', 'Centro Tutorial Rionegro'),
        ('Centro Tutorial Apartadó', 'Centro Tutorial Apartadó'),
    ])
    
    programa = models.CharField(max_length=100, choices=[
        ('Administración de Empresas', 'Administración de Empresas'),
        ('Administración de Mercadeo', 'Administración de Mercadeo'),
        ('Administración de Negocios Internacionales', 'Administración de Negocios Internacionales'),
        ('Administración de Obras Civiles', 'Administración de Obras Civiles'),
        ('Administración Turística y Hotelera', 'Administración Turística y Hotelera'),
        ('Derecho', 'Derecho'),
        ('Especialización en Gerencia de Mercadeo', 'Especialización en Gerencia de Mercadeo'),
        ('Especialización en gerencia del talento Humano', 'Especialización en gerencia del talento Humano'),
        ('Especialización en Evaluación y Gerencia de Proyectos', 'Especialización en Evaluación y Gerencia de Proyectos'),
        ('Especialización en Rehabilitación Cardiopulmonar', 'Especialización en Rehabilitación Cardiopulmonar'),
        ('Especialización de Sanidad Animal', 'Especialización de Sanidad Animal'),
        ('Ingeniería Administrativa', 'Ingeniería Administrativa'),
        ('Ingeniería de software', 'Ingeniería de software'),
        ('Medicina', 'Medicina'),
        ('Medicina Veterinaria y Zootecnia', 'Medicina Veterinaria y Zootecnia'),
        ('Odontología', 'Odontología'),
        ('Profesional en Mercadeo y Publicidad', 'Profesional en Mercadeo y Publicidad'),
        ('Tecnología en Gestión Empresarial', 'Tecnología en Gestión Empresarial'),
        ('Tecnología en Laboratorio de Prótesis Dental', 'Tecnología en Laboratorio de Prótesis Dental'),
        ('Terapia Respiratoria', 'Terapia Respiratoria'),
        
        
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
    TemasEventos = observaciones = models.TextField(blank=True)
    AreasBienestar = observaciones = models.TextField(blank=True)
    OtrasActividades = models.TextField()
    observaciones = models.TextField(blank=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now)


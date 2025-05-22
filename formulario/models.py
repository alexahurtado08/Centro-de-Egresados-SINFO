from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class DatosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación con el usuario

    nombre_completo = models.CharField(max_length=200)
    cédula = models.CharField(max_length=20)
    año_de_graduacion = models.IntegerField()
    
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
    
    genero = models.CharField(max_length=10, choices=[
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro'),
    ])
    
    celular = models.CharField(max_length=20)
    correo = models.EmailField()
    país_de_residencia = CountryField(blank_label='Seleccione un país')
    ciudad_de_residencia = models.CharField(max_length=100, blank=True)
    temas_eventos = models.CharField(max_length=10, choices=[
        ('Cursos', 'Cursos'),
        ('Diplomados', 'Diplomados'),
        ('Talleres', 'Talleres'),
    ])
    areas_bienestar = models.CharField(max_length=50, choices=[
        ('Deporte', 'Deporte'),
        ('Recreación', 'Recreación'),
        ('Cultura', 'Cultura'),
        ('Salud', 'Salud'),
        ('Desarrollo Humano', 'Desarrollo Humano'),
        ('Promoción Socioeconómica', 'Promoción Socioeconómica'),
    ])
    otras_actividades = models.TextField()
    tipo_evento = models.CharField(max_length=50, choices=[
        ('Académico-Social', 'Académico-Social'),
        ('Académico-Cultural', 'Académico-Cultural'),
        ('Socio-Cultural', 'Socio-Cultural'),
        ('Otro', 'Otro'),
    ])
    modalidad_evento = models.CharField(max_length=10, choices=[
        ('Presencial', 'Presencial'),
        ('Virtual', 'Virtual'),
        ('Mixto', 'Mixto'),
    ])
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.nombre_completo}"

# Generated by Django 5.2.1 on 2025-05-22 07:04

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=200)),
                ('cédula', models.CharField(max_length=20)),
                ('año_de_graduacion', models.IntegerField()),
                ('sede', models.CharField(choices=[('Medellín', 'Medellín'), ('Pereira', 'Pereira'), ('Rionegro', 'Centro tutorial Rionegro'), ('Apartado', 'Centro tutorial Apartado')], max_length=50)),
                ('programa', models.CharField(choices=[('Administración de empresas', 'Administración de empresas'), ('Administración de Mercadeo', 'Administración de Mercadeo'), ('Administración de negocios Internacionales', 'Administración de negocios Internacionales'), ('Administración Turística y Hotelera', 'Administración Turística y Hotelera'), ('Derecho', 'Derecho'), ('Especialización en Gerencia de Mercadeo', 'Especialización en Gerencia de Mercadeo'), ('Especialización en gerencia del talento Humano', 'Especialización en gerencia del talento Humano'), ('Especialización de Sanidad Animal', 'Especialización de Sanidad Animal'), ('Ingeniería Administrativa', 'Ingeniería Administrativa'), ('Ingeniería de software', 'Ingeniería de software'), ('Medicina', 'Medicina')], max_length=100)),
                ('genero', models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino'), ('Otro', 'Otro')], max_length=10)),
                ('celular', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('país_de_residencia', django_countries.fields.CountryField(max_length=2)),
                ('ciudad_de_residencia', models.CharField(blank=True, max_length=100)),
                ('temas_eventos', models.CharField(choices=[('Cursos', 'Cursos'), ('Diplomados', 'Diplomados'), ('Talleres', 'Talleres')], max_length=10)),
                ('areas_bienestar', models.CharField(choices=[('Deporte', 'Deporte'), ('Recreación', 'Recreación'), ('Cultura', 'Cultura'), ('Salud', 'Salud'), ('Desarrollo Humano', 'Desarrollo Humano'), ('Promoción Socioeconómica', 'Promoción Socioeconómica')], max_length=50)),
                ('otras_actividades', models.TextField()),
                ('tipo_evento', models.CharField(choices=[('Académico-Social', 'Académico-Social'), ('Académico-Cultural', 'Académico-Cultural'), ('Socio-Cultural', 'Socio-Cultural'), ('Otro', 'Otro')], max_length=50)),
                ('modalidad_evento', models.CharField(choices=[('Presencial', 'Presencial'), ('Virtual', 'Virtual'), ('Mixto', 'Mixto')], max_length=10)),
                ('observaciones', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

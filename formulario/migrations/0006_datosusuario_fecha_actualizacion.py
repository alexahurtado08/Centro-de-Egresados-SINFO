# Generated by Django 5.2.1 on 2025-05-26 23:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0005_alter_datosusuario_areasbienestar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosusuario',
            name='fecha_actualizacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

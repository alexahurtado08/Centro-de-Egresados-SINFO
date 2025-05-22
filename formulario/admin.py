from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import DatosUsuario

class DatosUsuarioResource(resources.ModelResource):
    class Meta:
        model = DatosUsuario

class DatosUsuarioAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = DatosUsuarioResource
    list_display = (
        'AñoGraduacion',
        'sede',
        'programa',
        'NombreCompleto',
        'cedula',
        'genero',
        'celular',
        'correo',
        'pais',
        'ciudad',
        'TemasEventos',
        'AreasBienestar',
        'OtrasActividades',
        'observaciones',
    )
    search_fields = ('NombreCompleto', 'cedula', 'correo')
    list_filter = ('sede', 'programa', 'genero')

admin.site.register(DatosUsuario, DatosUsuarioAdmin)
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
        'user',
        'nombre_completo',
        'cédula',
        'año_de_graduacion',
        'sede',
        'programa',
        'genero',
        'celular',
        'correo',
        'país_de_residencia',
        'ciudad_de_residencia',
        'temas_eventos',
        'areas_bienestar',
        'tipo_evento',
        'modalidad_evento',
    )
    search_fields = ('nombre_completo', 'cédula', 'correo')
    list_filter = ('sede', 'programa', 'genero', 'modalidad_evento')

admin.site.register(DatosUsuario, DatosUsuarioAdmin)

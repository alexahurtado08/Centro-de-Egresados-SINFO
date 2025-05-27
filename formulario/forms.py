# formulario/forms.py
from django import forms
from .models import DatosUsuario
from .models import ImagenFormulario


from django import forms
from .models import DatosUsuario

class DatosUsuarioForm(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        exclude = ['user']

        labels = {
            'AñoGraduacion': 'Año de graduación',
            'sede': 'Sede a la que pertenece',
            'programa': 'Programa o programas de los que egresó',
            'NombreCompleto': 'Nombres y apellidos completos',
            'cedula': 'Número de Cédula (sin puntos ni comas)',
            'genero': 'Género',
            'celular': 'Teléfono celular (sin puntos ni comas)',
            'correo': 'Correo electrónico personal',
            'pais': 'País de residencia',
            'ciudad': 'Ciudad de residencia',
            'TemasEventos': 'Temas de interés',
            'AreasBienestar': 'Áreas de bienestar',
            'OtrasActividades': 'Otras actividades',
            'observaciones': 'Observaciones y sugerencias',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Campos que deben ser solo lectura para el estudiante
        campos_solo_lectura = ['NombreCompleto', 'cedula', 'sede', 'programa']

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

            if field_name in campos_solo_lectura:
                self.fields[field_name].disabled = True  # Esto los hace "solo lectura"

            
            
class CargarExcelForm(forms.Form):
    archivo_excel = forms.FileField()
    


class ImagenFormularioForm(forms.ModelForm):
    class Meta:
        model = ImagenFormulario
        fields = ['titulo', 'imagen']
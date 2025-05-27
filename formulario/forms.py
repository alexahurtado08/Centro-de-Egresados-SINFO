# formulario/forms.py
from django import forms
from .models import DatosUsuario
from .models import ImagenFormulario


class DatosUsuarioForm(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        exclude = ['user']
        
        labels = {
            'AñoGraduacion': 'Año de graduación',
            'sede': 'Sede a la que pertenece',
            'programa': 'Programa o programas de los que egresó',
            'NombreCompleto': 'Nombres y apellidos completos',
            'cédula': 'Cédula sin puntos ni comas',
            'genero': 'Género',
            'celular': 'Teléfono celular sin puntos ni comas',
            'correo': 'Correo electrónico personal',
            'pais': 'País de residencia',
            'ciudad': 'Ciudad de residencia',
            'TemasEventos': 'Qué temas le gustaría que se desarrollaran en los eventos académicos o de educación continua para su actualización?',
            'AreasBienestar': 'Indique en que áreas le gustaría que se desarrollaran actividades de bienestar institucional dirigidas a los egresados',
            'OtrasActividades': 'Indique que otras actividades y/o beneficios le gustaría que la institución le brinde como egresado',
            'observaciones': 'Observaciones y sugerencias',
        }

    def __init__(self, *args, **kwargs):
        super(DatosUsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
            
class CargarExcelForm(forms.Form):
    archivo_excel = forms.FileField()
    


class ImagenFormularioForm(forms.ModelForm):
    class Meta:
        model = ImagenFormulario
        fields = ['titulo', 'imagen']
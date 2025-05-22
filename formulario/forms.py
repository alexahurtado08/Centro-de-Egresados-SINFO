# formulario/forms.py
from django import forms
from .models import DatosUsuario

class DatosUsuarioForm(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        exclude = ['user']
        
        labels = {
            'nombre_completo': 'Nombres y apellidos completos',
            'cédula': 'Cédula sin puntos ni comas',
            'año_de_graduacion': 'Año de graduación',
            'sede': 'Sede a la que pertenece',
            'programa': 'Programa o programas de los que egresó',
            'genero': 'Género',
            'celular': 'Teléfono celular sin puntos ni comas',
            'correo': 'Correo electrónico personal',
            'país_de_residencia': 'País de residencia',
            'ciudad_de_residencia': 'Ciudad de residencia',
            'temas_eventos': 'Qué temas le gustaría que se desarrollaran en los eventos académicos o de educación continua para su actualización?',
            'areas_bienestar': 'Indique en que áreas le gustaría que se desarrollaran actividades de bienestar institucional dirigidas a los egresados',
            'otras_actividades': 'Indique que otras actividades y/o beneficios le gustaría que la institución le brinde como egresado',
            'tipo_evento': 'Indique en que tipo de evento para el encuentro de egresados le gustaría participar',
            'modalidad_evento': 'Indique en cual modalidad le gustaría que se realice el encuentro de egresados',
            'observaciones': 'Observaciones y sugerencias',
        }

    def __init__(self, *args, **kwargs):
        super(DatosUsuarioForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

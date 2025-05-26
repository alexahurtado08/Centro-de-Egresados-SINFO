import django_filters
from .models import DatosUsuario

class DatosUsuarioFilter(django_filters.FilterSet):
    cedula = django_filters.CharFilter(lookup_expr='icontains', label='Cédula')

    class Meta:
        model = DatosUsuario
        fields = {
            'AñoGraduacion': ['exact'],
            'sede': ['exact'],
            'programa': ['exact'],
        }

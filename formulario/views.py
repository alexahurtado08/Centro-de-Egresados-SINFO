# formulario/views.py
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import DatosUsuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from import_export.formats.base_formats import XLSX
from .admin import DatosUsuarioResource
import pandas as pd
from .forms import CargarExcelForm
from django.contrib.auth.models import User
import pandas as pd
from .forms import DatosUsuarioForm
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.db.models import Count
from .models import ImagenFormulario
from .filters import DatosUsuarioFilter

@login_required
def formulario(request):
    try:
        datos_usuario = DatosUsuario.objects.get(user=request.user)
    except DatosUsuario.DoesNotExist:
        datos_usuario = None

    if request.method == 'POST':
        form = DatosUsuarioForm(request.POST, instance=datos_usuario)
        if form.is_valid():
            datos = form.save(commit=False)
            datos.user = request.user
            datos.save()
            return redirect('home')
    else:
        form = DatosUsuarioForm(instance=datos_usuario)

    # Obtener la última imagen cargada
    imagen_obj = ImagenFormulario.objects.last()
    imagen_url = imagen_obj.imagen.url if imagen_obj and imagen_obj.imagen else None

    return render(request, 'formulario/formulario.html', {'form': form, 'imagen_url': imagen_url})


def lista_datos_usuarios(request):
    datos = DatosUsuario.objects.all()
    filtro = DatosUsuarioFilter(request.GET, queryset=datos)
    return render(request, 'formulario/lista_datos_usuarios.html', {'filter': filtro})


def exportar_excel(request):
    resource = DatosUsuarioResource()
    dataset = resource.export()

    xlsx_format = XLSX()
    export_data = xlsx_format.export_data(dataset)

    response = HttpResponse(export_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="base_datos_usuarios.xlsx"'
    return response


def cargar_excel(request):
    if request.method == 'POST' and request.FILES.get('archivo_excel'):
        archivo = request.FILES['archivo_excel']
        try:
            df = pd.read_excel(archivo)

            for _, row in df.iterrows():
                user, created = User.objects.get_or_create(username=row['cedula'],defaults={'email': row['cedula']})

                if created:
                    user.set_password(str(row['cedula']))  # Usa la cédula como contraseña
                    user.save()

                
                DatosUsuario.objects.update_or_create(
                    user=user,
                    defaults={
                        'AñoGraduacion': row['AñoGraduacion'],
                        'sede': row['sede'],
                        'programa': row['programa'],
                        'NombreCompleto': row['NombreCompleto'],
                        'cedula': row['cedula'],
                        'genero': row['genero'],
                        'celular': str(row['celular']),
                        'correo': row['correo'],
                        'pais': row['pais'],
                        'ciudad': row['ciudad'],
                        'TemasEventos': row['TemasEventos'],
                        'AreasBienestar': row['AreasBienestar'],
                        'OtrasActividades': row['OtrasActividades'],
                        'observaciones': row.get('observaciones', '')
                    }
                )
            messages.success(request, "Archivo cargado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al cargar el archivo: {e}")
    
    return redirect('lista_usuarios')  # o al template que uses



def dashboard(request):
    # Total egresados por año
    egresados_por_anio = (
        DatosUsuario.objects
        .values('AñoGraduacion')
        .annotate(total=Count('id'))
        .order_by('AñoGraduacion')
    )

    # Total egresados por programa
    egresados_por_programa = (
        DatosUsuario.objects
        .values('programa')
        .annotate(total=Count('id'))
        .order_by('programa')
    )

    # Total egresados por país
    egresados_por_pais = (
        DatosUsuario.objects
        .values('pais')
        .annotate(total=Count('id'))
        .order_by('pais')
    )

    context = {
        'egresados_por_anio': list(egresados_por_anio),
        'egresados_por_programa': list(egresados_por_programa),
        'egresados_por_pais': list(egresados_por_pais),
    }

    return render(request, 'formulario/dashboard.html', context)




def datosusuario_editar(request, pk):
    dato = get_object_or_404(DatosUsuario, pk=pk)
    if request.method == 'POST':
        form = DatosUsuarioForm(request.POST, instance=dato)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')  # Ajusta esto
    else:
        form = DatosUsuarioForm(instance=dato)
    return render(request, 'formulario/editar_egresado.html', {'form': form})


@require_POST
def datosusuario_eliminar(request, pk):
    dato = get_object_or_404(DatosUsuario, pk=pk)
    dato.delete()
    return redirect('lista_usuarios')  # Ajusta esto
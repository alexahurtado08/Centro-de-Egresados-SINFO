# formulario/views.py
from django.shortcuts import render, redirect
from .forms import DatosUsuarioForm
from .models import DatosUsuario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from import_export.formats.base_formats import XLSX
from .admin import DatosUsuarioResource

@login_required
def formulario(request):
    try:
        datos = DatosUsuario.objects.get(user=request.user)
    except DatosUsuario.DoesNotExist:
        datos = None

    if request.method == 'POST':
        form = DatosUsuarioForm(request.POST, instance=datos)
        if form.is_valid():
            datos_usuario = form.save(commit=False)
            datos_usuario.user = request.user
            datos_usuario.save()
            return redirect('home')  
    else:
        form = DatosUsuarioForm(instance=datos)

    return render(request, 'formulario/formulario.html', {'form': form})


def lista_datos_usuarios(request):
    datos = DatosUsuario.objects.all()  # obtiene todos los registros
    return render(request, 'formulario/lista_datos_usuarios.html', {'datos': datos})





def exportar_excel(request):
    resource = DatosUsuarioResource()
    dataset = resource.export()

    xlsx_format = XLSX()
    export_data = xlsx_format.export_data(dataset)

    response = HttpResponse(export_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="base_datos_usuarios.xlsx"'
    return response
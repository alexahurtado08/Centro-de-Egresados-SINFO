# formulario/views.py
from django.shortcuts import render, redirect
from .forms import DatosUsuarioForm
from .models import DatosUsuario
from django.contrib.auth.decorators import login_required

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Perfil
from django.contrib.auth.decorators import login_required
from formulario.models import ImagenFormulario
from formulario.forms import ImagenFormularioForm

def inicio(request):
    return render(request, 'inicio.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "¡Has iniciado sesión exitosamente!")

            # Redirección condicional
            if user.is_superuser:
                return redirect('admin_home')  # Vista para el administrador
            else:
                return redirect('home')  # Vista para usuario normal
        else:
            messages.error(request, "Hubo un error al iniciar sesión, intenta de nuevo.")
            return redirect('login')

    return render(request, 'login.html')

def logout_user(request):
	django_logout(request)
	messages.success(request, ("¡Cerraste sesión correctamente!"))
	return redirect('inicio')



@login_required
def admin_home(request):
    return render(request, 'admin_home.html')



def editar_imagen_formulario(request):
    # Obtiene la primera imagen o None si no existe
    imagen_instance = ImagenFormulario.objects.first()

    if request.method == 'POST':
        form = ImagenFormularioForm(request.POST, request.FILES, instance=imagen_instance)
        if form.is_valid():
            form.save()
            return redirect('admin_home')  # Redirige a admin_home después de guardar
    else:
        form = ImagenFormularioForm(instance=imagen_instance)

    return render(request, 'editar_imagen_formulario.html', {'form': form})

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def crear_usuario_admin(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Asegura que el usuario esté activo
            user.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect('admin_home')
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = RegisterUserForm()
    return render(request, 'crear_usuario_admin.html', {'form': form})


from formulario.models import DatosUsuario
from formulario.forms import DatosUsuarioForm
from .forms import RegisterUserForm, DatosUsuarioFormAdmin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.is_superuser or user.is_staff

@user_passes_test(es_admin)
def registrar_usuario_completo(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        datos_form = DatosUsuarioFormAdmin(request.POST)

        if user_form.is_valid() and datos_form.is_valid():
            user = user_form.save()
            datos_usuario = datos_form.save(commit=False)
            datos_usuario.user = user
            datos_usuario.save()

            messages.success(request, "Usuario y datos registrados correctamente.")
            return redirect('admin_home')  # O a donde quieras redirigir

    else:
        user_form = RegisterUserForm()
        datos_form = DatosUsuarioFormAdmin()

    return render(request, 'User/registro_completo_admin.html', {
    'user_form': user_form,
    'datos_form': datos_form
})
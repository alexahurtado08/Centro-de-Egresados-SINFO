# Importaciones necesarias para vistas, autenticación y formularios
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

# Formularios y modelos propios
from .forms import RegisterUserForm, DatosUsuarioFormAdmin
from .models import Perfil
from formulario.models import ImagenFormulario, DatosUsuario
from formulario.forms import ImagenFormularioForm, DatosUsuarioForm

# Vista de página principal pública
def inicio(request):
    return render(request, 'inicio.html')

# Vista para iniciar sesión
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "¡Has iniciado sesión exitosamente!")

            # Redirige según si es administrador o usuario normal
            return redirect('admin_home' if user.is_superuser else 'home')
        else:
            messages.error(request, "Hubo un error al iniciar sesión, intenta de nuevo.")
            return redirect('login')

    return render(request, 'login.html')

# Vista para cerrar sesión
def logout_user(request):
    django_logout(request)
    messages.success(request, "¡Cerraste sesión correctamente!")
    return redirect('inicio')

# Vista del panel principal para administradores (requiere login)
@login_required
def admin_home(request):
    return render(request, 'admin_home.html')

# Vista para editar la imagen mostrada en el formulario
def editar_imagen_formulario(request):
    imagen_instance = ImagenFormulario.objects.first()

    if request.method == 'POST':
        form = ImagenFormularioForm(request.POST, request.FILES, instance=imagen_instance)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = ImagenFormularioForm(instance=imagen_instance)

    return render(request, 'editar_imagen_formulario.html', {'form': form})

# Vista para que un administrador cree un nuevo usuario básico
@staff_member_required
def crear_usuario_admin(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect('admin_home')
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = RegisterUserForm()
    return render(request, 'crear_usuario_admin.html', {'form': form})

# Verificación personalizada: solo admins o staff
def es_admin(user):
    return user.is_superuser or user.is_staff

# Vista para registrar tanto el usuario como sus datos personales (admin)
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
            return redirect('admin_home')

    else:
        user_form = RegisterUserForm()
        datos_form = DatosUsuarioFormAdmin()

    return render(request, 'User/registro_completo_admin.html', {
        'user_form': user_form,
        'datos_form': datos_form
    })

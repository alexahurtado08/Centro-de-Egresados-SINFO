from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

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
			return redirect('home')
		else:
			messages.success(request, ("Hubo un error al iniciar sesión, intenta de nuevo."))	
			return redirect('login')	


	else:
		return render(request, 'login.html', {})

def logout_user(request):
	django_logout(request)
	messages.success(request, ("¡Cerraste sesión correctamente!"))
	return redirect('inicio')


def registro(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()  # Solo guardamos el usuario, sin autenticación
            messages.success(request, "Registro exitoso. Ahora inicia sesión.")
            return redirect('home')  
    else:
        form = RegisterUserForm()

    return render(request, 'registro.html', {'form': form})


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from formulario.models import DatosUsuario
from User.validators import UsernameEqualsPasswordValidator
import re

# Formulario de registro de usuario personalizado
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')
        labels = {
            'first_name': 'Nombre',
            'username': 'Número de cédula',
        }

    # Validación personalizada del campo 'username' (cédula)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise ValidationError("La cédula es obligatoria.")
        if not re.fullmatch(r'\d{8,10}', username):
            raise ValidationError("La cédula debe tener entre 8 y 10 dígitos numéricos.")
        return username

    # Validación general del formulario
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")

        # Aplica validador personalizado para contraseña
        if username and password1:
            validator = UsernameEqualsPasswordValidator()

            # Objeto temporal para validar el username con la contraseña
            class TempUser:
                def __init__(self, username):
                    self.username = username

            temp_user = TempUser(username)

            try:
                validator.validate(password1, temp_user)
            except ValidationError as e:
                self.add_error('password1', e)

        return cleaned_data


# Formulario para registrar información adicional del usuario (admin)
class DatosUsuarioFormAdmin(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = ['NombreCompleto', 'cedula', 'programa', 'sede', 'AñoGraduacion']
        labels = {
            'AñoGraduacion': 'Año de graduación',
            'sede': 'Sede a la que pertenece',
            'programa': 'Programa o programas de los que egresó',
            'NombreCompleto': 'Nombres y apellidos completos',
            'cedula': 'Cédula sin puntos ni comas',
        }

    # Asigna clase CSS a los campos del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

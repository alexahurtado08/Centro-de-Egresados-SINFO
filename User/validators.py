# User/validators.py

# Excepciones de validación y traducción de mensajes
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# Validador personalizado para contraseñas
class UsernameEqualsPasswordValidator:
    def validate(self, password, user=None):
        # Verifica que el usuario esté definido y tenga un nombre de usuario
        if user is None or not user.username:
            return

        # Valida que la contraseña sea exactamente igual al nombre de usuario
        if password != user.username:
            raise ValidationError(
                _("La contraseña debe ser igual al nombre de usuario (cédula)."),
                code='password_mismatch',
            )

        # Valida que la contraseña tenga entre 8 y 10 caracteres
        if len(password) < 8 or len(password) > 10:
            raise ValidationError(
                _("La contraseña debe tener entre 8 y 10 caracteres."),
                code='password_length',
            )

    # Mensaje de ayuda para mostrar en formularios
    def get_help_text(self):
        return _("La contraseña debe ser igual al nombre de usuario y tener entre 8 y 10 caracteres.")

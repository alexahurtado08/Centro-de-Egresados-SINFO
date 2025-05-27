# User/validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class UsernameEqualsPasswordValidator:
    def validate(self, password, user=None):
        if user is None or not user.username:
            return

        if password != user.username:
            raise ValidationError(
                _("La contraseña debe ser igual al nombre de usuario (cédula)."),
                code='password_mismatch',
            )

        if len(password) < 8 or len(password) > 10:
            raise ValidationError(
                _("La contraseña debe tener entre 8 y 10 caracteres."),
                code='password_length',
            )

    def get_help_text(self):
        return _("La contraseña debe ser igual al nombre de usuario y tener entre 8 y 10 caracteres.")

from django.core.management.base import BaseCommand
from django.utils import timezone
from formulario.models import DatosUsuario
from django.core.mail import send_mail, EmailMessage
from datetime import timedelta

class Command(BaseCommand):
    help = 'Verifica si usuarios deben ser contactados y envía correo'

    def handle(self, *args, **kwargs):
        hoy = timezone.now().date()
        hace_un_ano = hoy - timedelta(days=365)

        usuarios = DatosUsuario.objects.filter(fecha_actualizacion__lte=hace_un_ano)
        '''
        for usuario in usuarios:
            email = EmailMessage(
                subject='Actualiza tu información como egresado',
                body=f'Hola {usuario.NombreCompleto},\n\nHa pasado un año desde tu última actualización. Por favor, ingresa a nuestro sistema para actualizar tus datos.\n\nGracias.',
                to=[usuario.correo],
            )
            email.send()
            usuario.fecha_actualizacion = hoy
            usuario.save()
        '''
        send_mail(
            subject='Actualiza tu información como egresado',
            message='Ha pasado un año desde tu última actualización. Por favor, ingresa a nuestro sistema para actualizar tus datos.',
            from_email='csalazara@eafit.edu.co',
            recipient_list=["csalazara@eafit.edu.co"],
        )
        self.stdout.write(self.style.SUCCESS(f'{usuarios.count()} correos enviados.'))
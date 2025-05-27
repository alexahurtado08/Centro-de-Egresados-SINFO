from django.urls import path
from . import views
from .views import editar_imagen_formulario
from .views import registrar_usuario_completo

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('editar-imagen-formulario/', editar_imagen_formulario, name='editar_imagen_formulario'),
    path('registro-completo/', views.registrar_usuario_completo, name='registro_completo_admin'),
    
]
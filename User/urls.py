from django.urls import path
from . import views
from .views import editar_imagen_formulario

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('editar-imagen-formulario/', editar_imagen_formulario, name='editar_imagen_formulario'),
]
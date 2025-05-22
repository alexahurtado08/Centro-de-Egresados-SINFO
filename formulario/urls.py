from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('usuarios/', views.lista_datos_usuarios, name='lista_usuarios'),
]

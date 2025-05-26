from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('usuarios/', views.lista_datos_usuarios, name='lista_usuarios'),
    path('exportar-excel/', views.exportar_excel, name='exportar_excel'),
    path('cargar-excel/', views.cargar_excel, name='cargar_excel'),
    path('dashboard/', views.dashboard, name='dashboard'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('formulario_registro/', views.registro, name='registro'),  # Ruta para el registro
    path('verificar-correo/<str:token>/', views.verificar_correo, name='verificar_correo'),  # Ruta para verificar el correo
]

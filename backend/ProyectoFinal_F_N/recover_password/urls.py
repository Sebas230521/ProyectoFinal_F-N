from django.urls import path
from .views import SolicitarRecuperacion, ConfirmarCodigo, CambiarContraseña

urlpatterns = [
    path('solicitar/', SolicitarRecuperacion.as_view(), name='solicitar_recuperacion'),
    path('confirmar/', ConfirmarCodigo.as_view(), name='confirmar_codigo'),
    path('cambiar/', CambiarContraseña.as_view(), name='cambiar_contraseña'),
]
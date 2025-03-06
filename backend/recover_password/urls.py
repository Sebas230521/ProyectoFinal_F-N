from django.urls import path
from .views import SolicitarRecuperacion, ConfirmarRecuperacion, CambiarContraseña

urlpatterns = [
    path('solicitar/', SolicitarRecuperacion.as_view(), name='solicitar_recuperacion'),
    path('confirmar/<str:token>/', ConfirmarRecuperacion.as_view(), name='confirmar_link'),  # Corregido
    path('cambiar/', CambiarContraseña.as_view(), name='cambiar_contraseña'),
]
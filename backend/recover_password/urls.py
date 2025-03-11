from django.urls import path
from .views import SolicitarRecuperacion, ConfirmarRecuperacion, RestablecerContraseña

urlpatterns = [
    path('solicitar/', SolicitarRecuperacion.as_view(), name='solicitar_recuperacion'),
<<<<<<< HEAD
    path('confirmar/', ConfirmarRecuperacion.as_view(), name='confirmar_recuperacion'),
    path('restablecer/', RestablecerContraseña.as_view(), name='restablecer_contraseña'),
]
=======
    path('confirmar/<str:token>/', ConfirmarRecuperacion.as_view(), name='confirmar_link'),  # Corregido
]
>>>>>>> 717431aa13641dc6fd1ab8ca5859f94c895921fa

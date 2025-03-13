from django.urls import path
from .views import SolicitarRecuperacion, ConfirmarRecuperacion, RestablecerContraseña

urlpatterns = [
    path('solicitar/', SolicitarRecuperacion.as_view(), name='solicitar_recuperacion'),
    path('confirmar/', ConfirmarRecuperacion.as_view(), name='confirmar_recuperacion'),
    path('restablecer/', RestablecerContraseña.as_view(), name='restablecer_contraseña'),
<<<<<<< HEAD
]

  
=======
]
>>>>>>> 1c199d0becb53c9e12f05d6f69d72d2d36e5b570

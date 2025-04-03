from django.urls import path
from .views import EstanquesPorUsuario, DetalleEstanqueView

urlpatterns = [
    path('estanques/', EstanquesPorUsuario.as_view(), name='estanques-usuario'),
    path('detalle_estanque/<int:pk>/', DetalleEstanqueView.as_view(), name='detalle-estanque'),
]

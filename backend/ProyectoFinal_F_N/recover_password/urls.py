from django.urls import path, include
from . import views

app_name = 'recover_password'  

urlpatterns = [
    path('solicitar/', views.solicitar_recuperacion, name='solicitar_recuperacion'),
    path('confirmar/', views.confirmar_codigo, name='confirmar_codigo'),
    path('cambiar/', views.cambiar_contraseña, name='cambiar_contraseña'),
    
]
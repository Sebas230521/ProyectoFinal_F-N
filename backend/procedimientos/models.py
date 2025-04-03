from django.db import models
from fish_management.models import Estanque  # Ajusta el path 

class Procedimientos(models.Model):
    CHOICES_TIPO_CONCENTRADO = [
    ('Alevinaje-45%', 'Alevinaje 45%'),
    ('PreJuveniles-38%', 'PreJuveniles 38%'),
    ('Juveniles-34%', 'Juveniles 34%'),
    ('PreEngorde-30%', 'PreEngorde 30%'),
    ('Engorde-24%', 'Engorde 24%'),
    ]
    
    nombre_finca = models.CharField(max_length=100)
    estanque = models.ForeignKey(Estanque, on_delete=models.CASCADE)
    tipoConcentrado = models.CharField(max_length=20, choices=CHOICES_TIPO_CONCENTRADO)
    nombreProcedimiento = models.CharField(max_length=100)
    descripcionProcedimiento = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombreProcedimiento} - {self.nombre_finca}"

from django.db import models
from fish_management.models import Estanque  # Ajusta el path según tu proyecto

class Procedimientos(models.Model):
    CHOICES_TIPO_CONCENTRADO = [
        ('Alevinaje', 'Alevinaje'),
        ('Juveniles', 'Juveniles'),
        ('Prejuveniles', 'Prejuveniles'),
        ('Engorde', 'Engorde'),
    ]
    
    responsable = models.CharField(max_length=100)
    estanque = models.ForeignKey(Estanque, on_delete=models.CASCADE, related_name="procedimientos")
    tipoConcentrado = models.CharField(max_length=20, choices=CHOICES_TIPO_CONCENTRADO)
    nombreProcedimiento = models.CharField(max_length=100)
    descripcionProcedimiento = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombreProcedimiento} - {self.responsable}"

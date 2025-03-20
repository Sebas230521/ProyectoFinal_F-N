from django.db import models
from registro.models import Usuario

class Estanque(models.Model):
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero_estanque = models.PositiveIntegerField()
    tipo_estanque = models.CharField(max_length=100)
    profundidad = models.FloatField()
    ancho = models.FloatField()
    largo = models.FloatField()
    especie_pez = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    numero_alimento = models.PositiveIntegerField()
    fecha_siembra = models.DateField()
    
    def __str__(self):
        return f"Estanque {self.numero_estanque}: {self.especie_pez} ({self.cantidad} peces)"
    
    class Meta:
        unique_together = ('id_user', 'numero_estanque')

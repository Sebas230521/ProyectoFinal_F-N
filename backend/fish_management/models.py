from django.db import models
from registro.models import Usuario

class Estanque(models.Model):
    id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_finca = models.CharField(max_length=100)
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
        return f"Finca {self.nombre_finca} - Estanque {self.numero_estanque}: {self.especie_pez} ({self.cantidad} peces)"

    class Meta:
        unique_together = ('id_user', 'nombre_finca', 'numero_estanque')  # 🔹 Restricción en la DB


# class Estanque(models.Model):
#     id_user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     nombre_finca = models.CharField(max_length=100)
#     numero_estanque = models.PositiveIntegerField()
#     tipo_estanque = models.CharField(max_length=100)
#     profundidad = models.FloatField()
#     ancho = models.FloatField()
#     largo = models.FloatField()
#     especie_pez = models.CharField(max_length=100)
#     cantidad = models.PositiveIntegerField()
#     numero_alimento = models.PositiveIntegerField()
#     fecha_siembra = models.DateField()

#     def __str__(self):
#         return f"Finca {self.nombre_finca} - Estanque {self.numero_estanque}: {self.especie_pez} ({self.cantidad} peces)"

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['id_user', 'nombre_finca', 'numero_estanque'], name='unique_estanque_finca')
#         ]

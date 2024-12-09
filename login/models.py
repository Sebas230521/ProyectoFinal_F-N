from django.db import models

class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=22,  # Ajustado para que soporte "pendiente_verificacion"
        choices=[
            ('activo', 'Activo'),
            ('pendiente_verificacion', 'Pendiente de Verificación')
        ]
    )
    fecha_registro = models.DateTimeField()

    class Meta:
        db_table = 'usuario'
        managed = False

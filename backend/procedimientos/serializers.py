from rest_framework import serializers
from .models import Procedimientos
from fish_management.models import Estanque  # Ajusta el path según tu proyecto

class ProcedimientosSerializer(serializers.ModelSerializer):
    # Usa PrimaryKeyRelatedField para seleccionar el estanque por su ID
    estanque = serializers.PrimaryKeyRelatedField(queryset=Estanque.objects.all())

    class Meta:
        model = Procedimientos
        fields = [
            'responsable',
            'estanque',
            'tipoConcentrado',
            'nombreProcedimiento',
            'descripcionProcedimiento',
            'observaciones',
            'fecha'
        ]
        read_only_fields = ['fecha']

    def validate_estanque(self, value):
        if not Estanque.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("El estanque seleccionado no existe. Por favor, ingrese un estanque válido.")
        return value

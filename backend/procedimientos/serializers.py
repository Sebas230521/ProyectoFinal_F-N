from rest_framework import serializers
from .models import Procedimientos
from fish_management.models import Estanque 

class ProcedimientosSerializer(serializers.ModelSerializer):
    # Se utiliza PrimaryKeyRelatedField para seleccionar el estanque por su ID
    estanque = serializers.PrimaryKeyRelatedField(queryset=Estanque.objects.all())

    class Meta:
        model = Procedimientos
        fields = [
            'nombre_finca',       
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

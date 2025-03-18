from rest_framework import serializers
from .models import Procedimientos, Fish

class ProcedimientosSerializer(serializers.ModelSerializer):
    estanque = serializers.PrimaryKeyRelatedField(queryset=Fish.objects.all())

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

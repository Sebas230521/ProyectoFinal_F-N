from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Estanque

class EstanqueSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = Estanque
        fields = [
            # id_user se asigna automáticamente desde request.user
            'numero_estanque',
            'tipo_estanque',
            'profundidad',
            'ancho',
            'largo',
            'especie_pez',
            'cantidad',
            'numero_alimento',
            'fecha_siembra'
        ]
        read_only_fields = ['id_user']
    
    def create(self, validated_data):
        # Asignamos id_user a partir del usuario autenticado en el request
        validated_data['id_user'] = self.context['request'].user
        return super().create(validated_data)

class EstanqueSerializerOutput(serializers.ModelSerializer):
    class Meta:
        model = Estanque
        fields = [
            'id_user',
            'numero_estanque',
            'tipo_estanque',
            'profundidad',
            'ancho',
            'largo',
            'especie_pez',
            'cantidad',
            'numero_alimento',
            'fecha_siembra'
        ]

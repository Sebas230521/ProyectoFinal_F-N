from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario 
        fields = ['nombre', 'correo_electronico', 'celular', 'password1', 'password2']

    def validate(self, data):
        """
        Valida que las contraseñas coincidan.
        """
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password1": "Las contraseñas no coinciden."})
        return data

    def create(self, validated_data):
        """
        Crea el usuario y hashea la contraseña.
        """
        validated_data.pop('password2')  # Eliminamos el campo password2
        user = Usuario.objects.create_user(
            nombre=validated_data['nombre'],
            correo_electronico=validated_data['correo_electronico'],
            celular=validated_data['celular'],
            password=validated_data['password1'],
            estado='Activo'  #se establece automaticamente
        )
        return user
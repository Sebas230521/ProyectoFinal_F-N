from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(serializers.Serializer):
    correo_electronico = serializers.EmailField()
    contrasena = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        correo_electronico = data.get("correo_electronico")
        contrasena = data.get("contrasena")

        # Verificar si el usuario existe en la base de datos
        try:
            usuario = Usuario.objects.get(correo_electronico=correo_electronico)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Correo o contraseña inválidos.")

        # Verificar si la contraseña es correcta
        if not check_password(contrasena, usuario.contrasena):
            raise serializers.ValidationError("Correo o contraseña inválidos.")

        # Generar el token JWT usando rest_framework_simplejwt
        refresh = RefreshToken.for_user(usuario)

        return {
            'correo_electronico': usuario.correo_electronico,
            'token': str(refresh.access_token),  # Retornamos el token de acceso
        }

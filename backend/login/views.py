from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from registro.models import Usuario
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.timezone import now
from rest_framework.views import APIView



class LoginView(APIView):
    authentication_classes = []  # No requiere autenticación
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

    def post(self, request):
        print("Datos recibidos en el backend:", request.data) 

        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            print("Errores de validación:", serializer.errors) 
            return Response({
                'mensaje': 'Error en el inicio de sesión',
                'errores': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            print("Usuario no encontrado con email:", email) 
            return Response({'mensaje': 'Correo o contraseña inválidos.'}, status=status.HTTP_400_BAD_REQUEST)

        if usuario.estado.lower() != 'activo':  
            print("Usuario no está activo:", usuario.estado)
            return Response({'mensaje': 'El usuario no está activo.'}, status=status.HTTP_400_BAD_REQUEST)

        if not check_password(password, usuario.password):
            print("Contraseña incorrecta para:", email) 
            return Response({'mensaje': 'Correo o contraseña inválidos.'}, status=status.HTTP_400_BAD_REQUEST)

        usuario.last_login = now()
        usuario.save(update_fields=['last_login'])

        refresh = RefreshToken.for_user(usuario)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        print("Login exitoso para:", email)

        return Response({
            'mensaje': 'Inicio de sesión exitoso',
            'email': usuario.email,
            'nombre': usuario.nombre,  # <-- Se recupera de la BD
            'access_token': access_token,
            'refresh_token': refresh_token
        }, status=status.HTTP_200_OK)
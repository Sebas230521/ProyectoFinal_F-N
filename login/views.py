from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class LoginView(APIView):
    """
    Vista para manejar el inicio de sesión de usuarios.
    """
    def post(self, request):
        # Crear el serializador con los datos recibidos
        serializer = LoginSerializer(data=request.data)
        
        # Validar los datos
        if serializer.is_valid():
            # Si los datos son válidos, devolver el token de acceso y el correo electrónico
            return Response({
                'mensaje': 'Inicio de sesión exitoso',
                'correo_electronico': serializer.validated_data['correo_electronico'],
                'token': serializer.validated_data['token']
            }, status=status.HTTP_200_OK)
        
        # Si la validación falla, devolver errores
        return Response({
            'mensaje': 'Error en el inicio de sesión',
            'errores': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        # Crear el serializador con los datos de la solicitud
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            # Si los datos son válidos, devolver el token y el correo electrónico
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Si los datos no son válidos, devolver los errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


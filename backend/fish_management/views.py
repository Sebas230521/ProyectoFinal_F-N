from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import EstanqueSerializerInput, EstanqueSerializerOutput
from .models import Estanque

class CreateEstanque(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            usuario = request.user
            numero_estanque = request.data.get("numero_estanque")

            # Verificar si ya existe un estanque con el mismo número para este usuario
            if Estanque.objects.filter(id_user=usuario, numero_estanque=numero_estanque).exists():
                return Response({'error': 'Ya existe un estanque con este número para este usuario.'},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = EstanqueSerializerInput(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(id_user=usuario)
                return Response(EstanqueSerializerOutput(serializer.instance).data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateEstanque(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk=None):
        try:
            usuario = request.user
            # Filtrar por id_user en lugar de usuario
            estanque_instance = Estanque.objects.get(pk=pk, id_user=usuario)

            serializer = EstanqueSerializerInput(estanque_instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(EstanqueSerializerOutput(serializer.instance).data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Estanque.DoesNotExist:
            return Response({'error': 'Estanque no encontrado o no tiene permisos.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ListEstanque(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user
        queryset = Estanque.objects.filter(id_user=usuario).order_by("fecha_siembra")
        serializer = EstanqueSerializerOutput(queryset, many=True)
        return Response(serializer.data)


class DetailsEstanque(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            usuario = request.user
            estanque_instance = Estanque.objects.get(pk=pk, id_user=usuario)
            serializer = EstanqueSerializerOutput(estanque_instance)
            return Response(serializer.data)
        except Estanque.DoesNotExist:
            return Response({'error': 'Estanque no encontrado o no tiene permisos.'}, status=status.HTTP_404_NOT_FOUND)

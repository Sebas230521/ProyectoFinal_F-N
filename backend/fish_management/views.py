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
            usuario = request.user  # Usuario autenticado
            numero_estanque = request.data.get("numero_estanque")  # Número de estanque
            nombre_finca = request.data.get("nombre_finca", "").strip().lower()# Nuevo campo: Nombre de la finca
            # Verificar si ya existe un estanque con el mismo número para este usuario
            print(f"Usuario: {usuario}, Nombre Finca: '{nombre_finca}', Número Estanque: {numero_estanque}")
            if Estanque.objects.filter(id_user=usuario, nombre_finca__iexact=nombre_finca, numero_estanque=numero_estanque).exists(): #hace que la búsqueda ignore mayúsculas y minúsculas.
                return Response({'error': 'Ya existe un estanque con este número para esta finca.'},
                    status=status.HTTP_400_BAD_REQUEST)

            # Serializar los datos de entrada
            serializer = EstanqueSerializerInput(data=request.data, context={'request': request})
            if serializer.is_valid():
                # Guardar el estanque, incluyendo el nombre de la finca
                serializer.save(id_user=usuario, nombre_finca=nombre_finca)
                return Response(EstanqueSerializerOutput(serializer.instance).data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateEstanque(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk=None):
        try:
            usuario = request.user
            # Buscar el estanque que pertenece al usuario autenticado
            estanque_instance = Estanque.objects.get(pk=pk, id_user=usuario)

            # Serializar los datos y permitir actualizaciones parciales (partial=True)
            serializer = EstanqueSerializerInput(estanque_instance, data=request.data, partial=True)
            if serializer.is_valid():
                # Si nombre_finca está en la solicitud, se actualiza; si no, mantiene su valor actual
                serializer.save(nombre_finca=request.data.get("nombre_finca", estanque_instance.nombre_finca))
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

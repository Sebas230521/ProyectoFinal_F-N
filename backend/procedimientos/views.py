from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Procedimientos
from .serializers import ProcedimientosSerializer

class CreateProcedimiento(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Si el frontend ya envía 'nombre_finca', no es necesario hacer cambios.
        # En caso contrario, podrías modificar request.data antes de serializar.
        serializer = ProcedimientosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Se crea el procedimiento
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProcedimiento(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, pk):
        try:
            procedimiento = Procedimientos.objects.get(pk=pk)
        except Procedimientos.DoesNotExist:
            return Response({'error': 'Procedimiento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProcedimientosSerializer(procedimiento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListProcedimientos(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        procedimientos = Procedimientos.objects.all()
        serializer = ProcedimientosSerializer(procedimientos, many=True)
        return Response(serializer.data)

class DetailsProcedimiento(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        try:
            procedimiento = Procedimientos.objects.get(pk=pk)
        except Procedimientos.DoesNotExist:
            return Response({'error': 'Procedimiento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProcedimientosSerializer(procedimiento)
        return Response(serializer.data)

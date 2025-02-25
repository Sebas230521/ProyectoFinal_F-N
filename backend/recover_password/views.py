from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from django.conf import settings
import random
from registro.models import Usuario
from .serializers import (
    SolicitarRecuperacionSerializer,
    ConfirmarCodigoSerializer,
    RecuperarContraseñaSerializer
)

class SolicitarRecuperacion(APIView):
    def post(self, request):
        serializer = SolicitarRecuperacionSerializer(data=request.data)
        if serializer.is_valid():
            correo_electronico = serializer.validated_data['correo_electronico']
            try:
                usuario = Usuario.objects.get(correo_electronico=correo_electronico)
                codigo = random.randint(1000, 9999)

                # Guardar código en la sesión
                request.session['codigo_recuperacion'] = codigo
                request.session['usuario_id'] = usuario.id
                request.session['codigo_creado_en'] = timezone.now().isoformat()

                # Enviar el código por correo
                send_mail(
                    'Código de recuperación de contraseña',
                    f'Tu código de recuperación es: {codigo}. Expira en 10 minutos.',
                    settings.EMAIL_HOST_USER,
                    [correo_electronico],
                    fail_silently=False,
                )

                return Response({'mensaje': 'Código enviado al correo electrónico.'}, status=status.HTTP_200_OK)

            except Usuario.DoesNotExist:
                return Response({'mensaje': 'Si el correo está registrado, recibirás un código de recuperación.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfirmarCodigo(APIView):
    def post(self, request):
        serializer = ConfirmarCodigoSerializer(data=request.data)
        if serializer.is_valid():
            codigo_usuario = serializer.validated_data['codigo']
            codigo_session = request.session.get('codigo_recuperacion')
            codigo_creado_en = request.session.get('codigo_creado_en')

            if not codigo_creado_en or not codigo_session:
                return Response({'error': 'Código no válido o expirado.'}, status=status.HTTP_400_BAD_REQUEST)

            # Convertir la fecha de creación
            codigo_creado_en = timezone.datetime.fromisoformat(codigo_creado_en)
            tiempo_expiracion = timedelta(minutes=settings.CODIGO_RECUPERACION_EXPIRA_MINUTOS)

            if timezone.now() > codigo_creado_en + tiempo_expiracion:
                request.session.flush()
                return Response({'error': 'El código ha expirado. Solicita uno nuevo.'}, status=status.HTTP_400_BAD_REQUEST)

            if codigo_usuario == codigo_session:
                return Response({'mensaje': 'Código válido. Procede a cambiar la contraseña.'}, status=status.HTTP_200_OK)

            return Response({'error': 'Código incorrecto.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CambiarContraseña(APIView):
    def post(self, request):
        serializer = RecuperarContraseñaSerializer(data=request.data)
        if serializer.is_valid():
            usuario_id = request.session.get('usuario_id')
            codigo_recuperacion = request.session.get('codigo_recuperacion')

            if not codigo_recuperacion:
                return Response({'error': 'Código no válido o expirado.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                usuario = Usuario.objects.get(id=usuario_id)

                # Guardar la nueva contraseña
                usuario.set_password(serializer.validated_data['nueva_contraseña'])
                usuario.save()

                # Limpiar la sesión
                request.session.flush()

                # Enviar correo de confirmación
                send_mail(
                    'Contraseña Cambiada con Éxito',
                    'Tu contraseña ha sido actualizada correctamente.',
                    settings.EMAIL_HOST_USER,
                    [usuario.correo_electronico],
                    fail_silently=False,
                )

                return Response({'mensaje': 'Contraseña cambiada exitosamente. Revisa tu correo.'}, status=status.HTTP_200_OK)

            except Usuario.DoesNotExist:
                return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.mail import send_mail
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from registro.models import Usuario
from .serializers import SolicitarRecuperacionSerializer, RecuperarContraseñaSerializer

signer = TimestampSigner()
from django.conf import settings  # Importar settings

class SolicitarRecuperacion(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SolicitarRecuperacionSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                usuario = Usuario.objects.get(email=email)

                # Generar el token único
                token = signer.sign(usuario.id)

                # Obtener la URL desde settings
                frontend_url = settings.FRONTEND_URL  
                reset_link = f"{frontend_url}/updatePassword?token={token}"

                # Enviar email con el enlace
                send_mail(
                    'Recuperación de contraseña',
                    f'Para restablecer tu contraseña, haz clic en el siguiente enlace: {reset_link}',
                    settings.EMAIL_HOST_USER,
                    [usuario.email],
                    fail_silently=False
                )

                return Response({"success": True, "message": "Si el correo existe, recibirás un enlace de recuperación."}, status=status.HTTP_200_OK)

            except Usuario.DoesNotExist:
                pass  # No revelar si el email existe o no

        return Response({"success": False, "message": "Solicitud inválida."}, status=status.HTTP_400_BAD_REQUEST)


# class SolicitarRecuperacion(APIView):
#     """Paso 1: El usuario envía su correo y el sistema genera un token."""
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = SolicitarRecuperacionSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             try:
#                 usuario = Usuario.objects.get(email=email)
#                 token = signer.sign(usuario.id)
#                 reset_link = f"http://frontend.com/reset-password?token={token}"
#                 send_mail(
#                     'Recuperación de contraseña',
#                     f'Para restablecer tu contraseña, haz clic en el siguiente enlace: {reset_link}',
#                     settings.EMAIL_HOST_USER,
#                     [usuario.email],
#                     fail_silently=False
#                 )
#                 return Response({"success": True, "message": "Si el correo existe, recibirás un enlace de recuperación."}, status=status.HTTP_200_OK)
#             except Usuario.DoesNotExist:
#                 pass  # No revelar si el email existe o no
#         return Response({"success": False, "message": "Solicitud inválida."}, status=status.HTTP_400_BAD_REQUEST)


class ConfirmarRecuperacion(APIView):
    """Paso 2: El frontend envía el token y el backend verifica si es válido."""
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({'success': False, 'message': 'Token no proporcionado.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            usuario_id = signer.unsign(token, max_age=600)
            return Response({"success": True, "message": "Token válido.", "token": token}, status=status.HTTP_200_OK)
        except (BadSignature, SignatureExpired):
            return Response({'success': False, 'message': 'El enlace es inválido o ha expirado.'}, status=status.HTTP_400_BAD_REQUEST)


class RestablecerContraseña(APIView):
    """Paso 3: El usuario proporciona el token y una nueva contraseña para restablecerla."""
    permission_classes = [AllowAny]

    def post(self, request):
        token = request.data.get("token")
        serializer = RecuperarContraseñaSerializer(data=request.data)
        if not token:
            return Response({'success': False, 'message': 'Token no proporcionado.'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            try:
                usuario_id = signer.unsign(token, max_age=600)
                usuario = Usuario.objects.get(id=usuario_id)
                usuario.set_password(serializer.validated_data['nueva_contraseña'])
                usuario.save()
                send_mail(
                    'Contraseña cambiada',
                    'Tu contraseña ha sido cambiada con éxito.',
                    settings.EMAIL_HOST_USER,
                    [usuario.email],
                    fail_silently=False
                )
                return Response({'success': True, 'message': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)
            except (BadSignature, SignatureExpired):
                return Response({'success': False, 'message': 'El enlace es inválido o ha expirado.'}, status=status.HTTP_400_BAD_REQUEST)
            except Usuario.DoesNotExist:
                return Response({'success': False, 'message': 'Usuario no encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

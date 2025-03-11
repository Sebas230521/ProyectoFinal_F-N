from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from registro.models import Usuario

from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.urls import reverse  # Para generar la URL del enlace

class SolicitarRecuperacion(APIView):
    def post(self, request):
        correo_electronico = request.data['correo_electronico']
        try:
            usuario = Usuario.objects.get(correo_electronico=correo_electronico)   # Generar un token firmado con el ID del usuario
            signer = TimestampSigner()
            token = signer.sign(usuario.id)  # Ejemplo: "45:sdf876sdf87dsf987"

            # Generar la URL de recuperación con el token
            url_recuperacion = request.build_absolute_uri(
                reverse('confirmar_link', kwargs={'token': token})
            )
            
            # Enviar el enlace por correo
            send_mail(
                'Recuperación de contraseña',
                f'Usa el siguiente enlace para restablecer tu contraseña: {url_recuperacion}\n\nEste enlace expira en 10 minutos.',
                settings.EMAIL_HOST_USER,
                [correo_electronico],
                fail_silently=False,
            )

            return Response({'mensaje': 'Se a  enviado un enlace de recuperacion al correo electrónico.'}, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:
            return Response({'mensaje': 'Si el correo está registrado, recibirás un enlace de recuperación.'}, status=status.HTTP_200_OK)



class ConfirmarRecuperacion(APIView):
    def post(self, request, token):
        signer = TimestampSigner() 
        
        try:
            # Verificar y desencriptar el token
            usuario_id = signer.unsign(token, max_age=600)  # Expira en 600 segundos (10 minutos)

            # Buscar al usuario en la base de datos
            usuario = Usuario.objects.get(id=usuario_id)

            nueva_contraseña = request.data['nueva_contraseña']
            confirmar_contraseña = request.data['confirmar_contraseña']
            
            if not nueva_contraseña or not confirmar_contraseña:
                return Response({'error': 'Faltan datos'}, status=status.HTTP_400_BAD_REQUEST)
            
            if nueva_contraseña != confirmar_contraseña:
                return Response({'mensaje': 'Las contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Actualizar la contraseña
            usuario.set_password(nueva_contraseña)
            usuario.save()
            
            send_mail(
                'contraseña cambiada',
                'Tu contraseña ha sido cambiada.',
                settings.EMAIL_HOST_USER,
                [usuario.correo_electronico],
                fail_silently=False,
            )
            
            return Response({'mensaje': 'Contraseña actualizada correctamente.'}, status=status.HTTP_200_OK)
        
        except(BadSignature, SignatureExpired):
            return Response({'error':'el enlace es invalido o ha expirado'},status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
        
    


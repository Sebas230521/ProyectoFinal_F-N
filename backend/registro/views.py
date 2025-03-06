from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UsuarioSerializer
from .models import Usuario
from django.core.mail import send_mail
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.conf import settings

# usamos TimestampSigner para agregar tiempo de expiración al token
signer = TimestampSigner()

@api_view(['POST'])
@permission_classes([AllowAny])
def registro(request):
    if request.method == 'POST':
        try:
            data = request.data
            serializer = UsuarioSerializer(data=data)

            # Validar el formato de los datos
            if not serializer.is_valid():
                return JsonResponse({
                    'error': 'Datos inválidos',
                    'details': serializer.errors
                }, status=400)

            # Validar que las contraseñas coincidan
            if data['password1'] != data['password2']:
                return JsonResponse({
                    'error': 'Las contraseñas no coinciden'
                }, status=400)

            # Creamos el usuario con estado "pendiente_verificacion"
            user = Usuario.objects.create_user(
                nombre=data['nombre'],
                correo_electronico=data['correo_electronico'],
                celular=data['celular'],
                password=data['password1'],
                estado='pendiente_verificacion'  # Correcto
            )

            # Genera el token firmado para ser usado en el correo
            token = signer.sign(user.correo_electronico)
            verificacion_url = f"{settings.FRONTEND_URL}/verify-email/{token}"

            # Enviar correo con el enlace de verificación
            send_mail(
                'Verifica tu cuenta',
                f'Hola {user.nombre}, verifica tu cuenta haciendo clic en el siguiente enlace: {verificacion_url}',
                settings.DEFAULT_FROM_EMAIL,
                [user.correo_electronico],
                fail_silently=False,
            )

            return JsonResponse({
                'mensaje': 'Usuario registrado correctamente. Revisa tu correo para verificar la cuenta.',
                'usuario_id': user.id
            }, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@api_view(['GET'])
@permission_classes([AllowAny])
def verificar_correo(request, token):
    try:
        # Verificar el token y extraer el correo (válido por 10 minutos)
        email = signer.unsign(token, max_age=600)

        # Buscar el usuario con el correo extraído
        user = Usuario.objects.get(correo_electronico=email)

        if user.estado == 'activo':
            return JsonResponse({'mensaje': 'El usuario ya está activado.'}, status=200)

        # Activar usuario
        user.estado = 'activo'
        user.save()

        return JsonResponse({'mensaje': 'Correo verificado con éxito. Ya puedes iniciar sesión.'}, status=200)

    except SignatureExpired:
        return JsonResponse({'error': 'El token ha expirado. Solicita otro enlace.'}, status=400)

    except BadSignature:
        return JsonResponse({'error': 'Token inválido.'}, status=400)

    except Usuario.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado.'}, status=400)

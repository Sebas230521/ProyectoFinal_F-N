from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.utils import timezone
from registro.models import Usuario
# Create your views here.

def solicitar_recuperacion(request):
    if request.method == 'POST':
        correo_electronico = request.POST.get('correo_electronico')
        try:
            usuario = Usuario.objects.get(correo_electronico=correo_electronico)
            codigo = random.randint(1000, 9999)
            
            # guardar el codigo,fecha y hora de sesion
            request.session['codigo_recuperacion'] = codigo
            request.session['usuario_id'] = usuario.id
            request.session['codigo_creado_en'] = timezone.now().isoformat()            
            # enviar el correo
            
            send_mail(
                'codigo de recuperación de contraseña',
                f'tu codigo de recuperacion es:{codigo}. Este codigo expira en 10 minutos.',
                settings.EMAIL_HOST_USER,
                [correo_electronico],
                fail_silently=False,
            )
            
            return redirect('password_reset:confirmar_codigo')
        except Usuario.DoesNotExist:
            return render(request, 'password_reset/recuperacion.html', {'error': 'El correo electrónico no está registrado.'})
    return render(request, 'password_reset/recuperacion.html')

def confirmar_codigo(request):
    if request.method == 'POST':
        codigo_usuario = request.POST.get('codigo')
        codigo_session = request.session.get('codigo_recuperacion')
        codigo_creado_en = request.session.get('codigo_creado_en')
        intentos = request.session.get('intentos', 0)
        
        if not codigo_creado_en:
            return render(request, 'password_reset/confirmar_codigo.html', {'error': 'Código no válido o expirado.'})

        # Convertir la cadena de fecha/hora a un objeto datetime
        codigo_creado_en = timezone.datetime.fromisoformat(codigo_creado_en)

        # Verificar si el código ha expirado (por ejemplo, después de 15 minutos)
        tiempo_expiracion = timedelta(minutes=settings.CODIGO_RECUPERACION_EXPIRA_MINUTOS)
        
        if timezone.now() > codigo_creado_en + tiempo_expiracion:
            del request.session['codigo_recuperacion']
            del request.session['codigo_creado_en']
            return render(request, 'password_reset/confirmar_codigo.html', {'error': 'El código ha expirado. Solicita uno nuevo.'})
        
        
        if int(codigo_usuario) == codigo_session:
            return redirect('password_reset:cambiar_contraseña')
        else:
            intentos += 1
            request.session['intentos'] = intentos
            if intentos > 6:
                # Limpiar la sesión si se superan los intentos
                del request.session['codigo_recuperacion']
                del request.session['codigo_creado_en']
                del request.session['intentos']
            return render(request, 'password_reset/confirmar_codigo.html', {'error': 'Código incorrecto. Intetalo de nuevo.'})
    return render(request, 'password_reset/confirmar_codigo.html')

def cambiar_contraseña(request):
    if request.method == 'POST':
        nueva_contraseña = request.POST.get('nueva_contraseña')
        usuario_id = request.session.get('usuario_id')
        codigo_recuperacion = request.session.get('codigo_recuperacion')
        
        # Verificar si el código de recuperación aún está en la sesión
        if not codigo_recuperacion:
            messages.error(request, 'Código no válido o expirado.')
            return redirect(request, 'password_reset:solicitar_recuperacion')

        try:
            usuario = Usuario.objects.get(id=usuario_id)
            usuario.set_password(nueva_contraseña)  # Encripta y guarda la nueva contraseña
            usuario.save()
        
            # Limpiar la sesión
            del request.session['codigo_recuperacion']
            del request.session['usuario_id']
            del request.session['codigo_creado_en']
            
            messages.success(request, 'Contraseña cambiada exitosamente. Por favor, inicia sesión con tu nueva contraseña.')
        
            return redirect('login')
        
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')
            return redirect('password_reset:solicitar_recuperacion')
    return render(request, 'password_reset/cambiar_contraseña.html')
        
    return render(request, 'password_reset/cambiar_contraseña.html')
        
        

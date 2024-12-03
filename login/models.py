from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, contrasena=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico debe ser proporcionado')
        usuario = self.model(correo_electronico=correo_electronico, **extra_fields)
        usuario.set_password(contrasena)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo_electronico, contrasena=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo_electronico, contrasena, **extra_fields)

class Usuario(AbstractBaseUser):
    correo_electronico = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=128)  # Este campo es el que se usa para almacenar las contraseñas
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.correo_electronico


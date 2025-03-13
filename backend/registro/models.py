""" from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, nombre, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        correo_electronico = self.normalize_email(correo_electronico)
        usuario = self.model(correo_electronico=correo_electronico, nombre=nombre, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo_electronico, nombre, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo_electronico, nombre, password, **extra_fields)

class Usuario(AbstractBaseUser):
    ESTADO = [
        ('activo', 'Activo'),
        ('pendiente_verificacion', 'Pendiente de Verificación'),
    ]

    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    correo_electronico = models.EmailField(unique=True)
    estado = models.CharField(max_length=30, choices=ESTADO, default='activo')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'usuario'
        managed = False """


from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, nombre, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El correo electrónico es obligatorio')
        correo_electronico = self.normalize_email(correo_electronico)
        usuario = self.model(correo_electronico=correo_electronico, nombre=nombre, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo_electronico, nombre, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(correo_electronico, nombre, password, **extra_fields)

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Usuario(AbstractBaseUser, PermissionsMixin):  # Agregar PermissionsMixin
    ESTADO = [
        ('activo', 'Activo'),
        ('pendiente_verificacion', 'Pendiente de Verificación'),
    ]

    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    correo_electronico = models.EmailField(unique=True)
    estado = models.CharField(max_length=30, choices=ESTADO, default='activo')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    # Agregar estos campos para permisos
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']

    def _str_(self):
        return self.nombre

    #  Métodos para permisos
    def has_perm(self, perm, obj=None):
        return self.is_superuser  # Los superusuarios tienen todos los permisos

    def has_module_perms(self, app_label):
        return self.is_superuser  # Los superusuarios pueden ver todos los módulos

    class Meta:
        db_table = 'usuario'
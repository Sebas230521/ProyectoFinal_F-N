# Generated by Django 4.2.9 on 2024-12-02 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estanque',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='historialactividad',
            name='id_estanque',
        ),
        migrations.RemoveField(
            model_name='inventarioalimento',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='observacion',
            name='id_estanque',
        ),
        migrations.RemoveField(
            model_name='observacion',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_registro',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=8.23451910408432e-05, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='contrasena',
            field=models.CharField(max_length=128),
        ),
        migrations.DeleteModel(
            name='Alimentacion',
        ),
        migrations.DeleteModel(
            name='Estanque',
        ),
        migrations.DeleteModel(
            name='HistorialActividad',
        ),
        migrations.DeleteModel(
            name='InventarioAlimento',
        ),
        migrations.DeleteModel(
            name='Observacion',
        ),
    ]

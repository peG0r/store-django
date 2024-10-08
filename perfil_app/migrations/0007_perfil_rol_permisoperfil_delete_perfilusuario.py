# Generated by Django 5.0.6 on 2024-05-28 17:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil_app', '0006_remove_perfil_rol'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='rol',
            field=models.CharField(choices=[('NU', 'Usuario Normal'), ('VE', 'Vendedor')], default='NU', max_length=2),
        ),
        migrations.CreateModel(
            name='PermisoPerfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puede_agregar', models.BooleanField(default=False)),
                ('puede_cambiar', models.BooleanField(default=False)),
                ('puede_eliminar', models.BooleanField(default=False)),
                ('puede_ver', models.BooleanField(default=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PerfilUsuario',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-27 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

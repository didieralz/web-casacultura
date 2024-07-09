# Generated by Django 5.0.6 on 2024-07-09 06:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0012_rename_nombre_estudiante_apellidos_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='usuario_relacionado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_relacionado', to=settings.AUTH_USER_MODEL),
        ),
    ]

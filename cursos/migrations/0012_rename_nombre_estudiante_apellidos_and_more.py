# Generated by Django 5.0.6 on 2024-07-09 06:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0011_alter_estudiante_fecha_nacimiento'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='nombre',
            new_name='apellidos',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='nombres',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='usuario_relacionado',
            field=models.ForeignKey(default='didier', on_delete=django.db.models.deletion.CASCADE, related_name='usuario_relacionado', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
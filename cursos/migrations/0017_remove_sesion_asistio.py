# Generated by Django 5.0.6 on 2024-07-10 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0016_sesion_asistio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sesion',
            name='asistio',
        ),
    ]

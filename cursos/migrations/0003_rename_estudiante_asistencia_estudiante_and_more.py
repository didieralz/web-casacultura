# Generated by Django 5.0.6 on 2024-07-05 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_rename_estudiante_asistencia_estudiante_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asistencia',
            old_name='Estudiante',
            new_name='estudiante',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='Cursos',
            new_name='cursos',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='Cursos',
            new_name='cursos',
        ),
        migrations.RenameField(
            model_name='matricula',
            old_name='Estudiante',
            new_name='estudiante',
        ),
    ]

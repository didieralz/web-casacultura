# Generated by Django 5.0.6 on 2024-07-06 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_rename_estudiante_asistencia_estudiante_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='image',
            field=models.FileField(blank=True, upload_to='cursos_images/'),
        ),
    ]

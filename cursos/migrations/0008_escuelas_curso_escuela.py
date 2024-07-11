# Generated by Django 5.0.6 on 2024-07-08 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0007_remove_categoria_cursos_curso_categorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escuelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='escuela',
            field=models.ManyToManyField(blank=True, related_name='cursos', to='cursos.escuelas'),
        ),
    ]
from django.contrib.auth.models import User #esta linea trae el sistema d eautenticacion de usuario por defecto de django
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Escuelas(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(blank=False)
    fecha_fin = models.DateField(blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.IntegerField()
    horas_semanales = models.IntegerField()
    image = models.FileField(upload_to="cursos_images/", blank=True)
    categorias = models.ManyToManyField(Categoria, related_name='cursos', blank=True)
    escuela = models.ForeignKey(Escuelas, related_name='cursos', null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
   
class Estudiante(models.Model):
    usuario = models.ForeignKey(User,related_name='usuario_relacionado', on_delete=models.CASCADE,default=1)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField(blank=False)
    sisben = models.CharField(max_length=3)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.usuario.username

    
class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.Estudiante} - {self.Curso}'
    
class Instructor(models.Model):
    nombre = models.CharField(max_length=200)
    bio = models.TextField()
    cursos = models.ManyToManyField(Curso, related_name='instructores')
    
    def __str__(self):
        return self.nombre
    
from django.db import models


    
class Sesion(models.Model):
    Curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='sesiones')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    
    def __str__(self):
        return f'Sesión de {self.Curso} el {self.fecha}'

class Asistencia(models.Model):
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, related_name='asistencias')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.Estudiante} - {self.sesion}'

    

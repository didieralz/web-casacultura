from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    capacidad = models.IntegerField()
    horas_semanales = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.usuario.username
    
class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.estudiante} - {self.curso}'
    
class Instructor(models.Model):
    nombre = models.CharField(max_length=200)
    bio = models.TextField()
    cursos = models.ManyToManyField(Curso, related_name='instructores')
    
    def __str__(self):
        return self.nombre
    
class Sesion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='sesiones')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    def __str__(self):
        return f'Sesión de {self.curso} el {self.fecha}'

class Asistencia(models.Model):
    sesion = models.ForeignKey(Sesion, on_delete=models.CASCADE, related_name='asistencias')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.estudiante} - {self.sesion}'
from django.contrib import admin
from cursos.models import Curso, Estudiante, Matricula, Instructor, Categoria, Sesion, Asistencia
# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Matricula)
admin.site.register(Instructor)
admin.site.register(Categoria)
admin.site.register(Sesion)
admin.site.register(Asistencia)
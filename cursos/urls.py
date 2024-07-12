from django.urls import path
from cursos import views

urlpatterns = [
    path("", views.Curso_index, name="curso_index"),
    path("<int:pk>/", views.Curso_detail, name="curso_detail"),
    path("registro_estudiante/",views.estudiante_new,name="estudiante_new"),
    path("estudiantes/",views.estudiante_list,name="estudiante_list"),
    
]
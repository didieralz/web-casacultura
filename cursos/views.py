# cursoss/views.py

from django.shortcuts import render
from cursos.models import Curso

# Create your views here.

def Curso_index(request):
    Cursos = Curso.objects.all()
    context = {
        "Cursos": Cursos
    }
    return render(request, "cursos/cursos_index.html", context)

def Curso_detail(request, pk):
    Curso = Curso.objects.get(pk=pk)
    context = {
        "Curso": Curso
    }
    return render(request, "cursos/cursos_detail.html", context)

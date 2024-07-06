# cursoss/views.py

from django.shortcuts import render
from cursos.models import Curso

# Create your views here.

def Curso_index(request):
    Cursos = Curso.objects.all()
    context = {
        "Cursos": Cursos
    }
    return render(request, "cursos/curso_index.html", context)

def Curso_detail(request, pk):
    curso = Curso.objects.get(pk=pk)
    context = {
        "Curso": curso
    }
    return render(request, "cursos/curso_detail.html", context)

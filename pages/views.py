# pages/views.py

from django.shortcuts import render
from cursos.models import Curso

# Create your views here.

def home(request):
    return render(request, "pages/home.html", {})


# intento crear un href en home para ir a index
# para lograrlo 1 creo la funcion  Curso_index en views

def Curso_index(request):
    Cursos = Curso.objects.all()
    context = {
        "Cursos": Cursos
    }
    return render(request, "cursos/curso_index.html", context)



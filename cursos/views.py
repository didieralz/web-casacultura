# cursoss/views.py

from django.shortcuts import render
from cursos.models import Curso
from . import forms

# Create your views here.

def Curso_index(request):
    query = request.GET.get('q')
    if query:
        Cursos = Curso.objects.filter(nombre__icontains=query)
    else:
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
 
def estudiante_new(request):
    form = forms.CreateEstudiante()
    context = {'form':form}
    return render(request,'cursos/estudiante_new.html',context)
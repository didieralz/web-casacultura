# cursoss/views.py

from django.shortcuts import render, redirect
from cursos.models import Curso,Estudiante
from django.contrib.auth.decorators import login_required #implmentarlogin required, en seting se debe poner login url
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

@login_required(login_url="login")
def estudiante_new(request):
    if request.method == 'POST':
        form = forms.CreateEstudiante(request.POST,request.FILES)#no estoy seguro de necesitar request.FILES ya que mi form no tiene archivos
        if form.is_valid():
            # save with user 
            newEstudiante = form.save(commit = False)
            newEstudiante.usuario = request.user
            newEstudiante.save()
            return redirect("estudiante_list") #hay que cambiar el redirect a la pagina de lista de estudiantes cuando exista
    else:
        form = forms.CreateEstudiante()
    context = {'form':form}
    return render(request,'cursos/estudiante_new.html',context)

@login_required(login_url="login")
def estudiante_list(request):
    Estudiantes = Estudiante.objects.filter(usuario=request.user)
    context = {
        "Estudiantes": Estudiantes
    }
    return render(request, "cursos/Estudiante_list.html", context)

@login_required(login_url="login")
def matricular(request):

    if request.method == 'POST':
        form = forms.MatricularEstudiante(request.POST,request.FILES)#no estoy seguro de necesitar request.FILES ya que mi form no tiene archivos
        form.fields["estudiante"].queryset = Estudiante.objects.filter(usuario=request.user.id) #intentando que solo muestre los estudantes del usuario
        if form.is_valid():
            newMatricula = form.save(commit = False)
            newMatricula.save()
            return redirect("estudiante_list") #hay que cambiar el redirect a la pagina de cursos matriculados
    else:
        form = forms.MatricularEstudiante()

    context = {'form':form}
    return render(request,'cursos/matricular.html',context)
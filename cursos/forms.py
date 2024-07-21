#https://www.youtube.com/watch?v=GQKKjrdS6pc&ab_channel=DaveGray
#https://realpython.com/django-social-forms-4/#step-10-submit-dweets-using-django-forms
#https://pythonassets.com/posts/date-field-with-calendar-widget-in-django-forms/

#para crear forms se crea este archivo, y se crean las clases que menjan cada form, luego se agrega en views  la forma como se manejara las views y finalmetne se genra el html
from django import forms
from . import models

class CreateEstudiante (forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = ['tipo_documento','documento','nombres','apellidos','fecha_nacimiento','sisben','direccion','telefono']
        widgets = {
            'fecha_nacimiento': forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }

class MatricularEstudiante (forms.ModelForm):
    class Meta:
        model = models.Matricula
        fields = ['estudiante','Curso']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MatricularEstudiante, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['estudiante'].queryset = models.Estudiante.objects.filter(usuario=user)
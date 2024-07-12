#https://www.youtube.com/watch?v=GQKKjrdS6pc&ab_channel=DaveGray
#https://realpython.com/django-social-forms-4/#step-10-submit-dweets-using-django-forms

#para crear forms se crea este archivo, y se crean las clases que menjan cada form, luego se agrega en views  la forma como se manejara las views y finalmetne se genra el html
from django import forms
from . import models

class CreateEstudiante (forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = ['nombres','apellidos','fecha_nacimiento','sisben','direccion','telefono']
#https://www.youtube.com/watch?v=GQKKjrdS6pc&ab_channel=DaveGray

#para crear forms se crea este archivo, y se crean las clases que menjan cada form, luego se agrega en views  la forma como se manejara las views y finalmetne se genra el html
from django import forms
from . import models

#hay que repensar la estructura como se crean estudiantes y matriculas
class CreateEstudiante (forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = ['usuario_relacionado','nombres','apellidos','fecha_nacimiento','sisben','direccion','telefono']
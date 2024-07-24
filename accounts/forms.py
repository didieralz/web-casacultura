from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Introduce una dirección de correo electrónico válida.',label="Correo")
    username = forms.CharField(max_length=150,min_length=4, help_text='Requerido. 150 caracteres maximo, entre letras, numeros y @/./+/-/_ .',label="Nombre de usuario")
    password1 = forms.CharField(max_length=150,min_length=8, help_text='Requerido. Al menos 8 caracteres, incluyendo letras y números.', widget=forms.PasswordInput,label="Contraseña")
    password2 = forms.CharField(max_length=32,min_length=8, help_text='Requerido. Debe coincidir con la contraseña anterior.', widget=forms.PasswordInput,label="Confirme su Contraseña")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "password1": forms.PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password1'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso. Por favor, elige otro.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso. Por favor, elige otro.")
        if not(bool(re.search('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email))):
            raise forms.ValidationError("Porfavor ingrese un correo valido")
        return email


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
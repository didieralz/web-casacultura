# pages/urls.py

from django.urls import path
from pages import views


urlpatterns = [
    path("", views.home, name='home'),
    path("index", views.Curso_index, name="curso_index"), # intento crear un href en home para ir a index
]
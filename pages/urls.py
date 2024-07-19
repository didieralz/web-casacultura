# pages/urls.py

from django.urls import path
from pages import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name='home'),
    path("index", views.Curso_index, name="curso_index"), # intento crear un href en home para ir a index
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
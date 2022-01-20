from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver_paciente/<int:id>', views.ver_pacientes, name="ver_pacientes")
]

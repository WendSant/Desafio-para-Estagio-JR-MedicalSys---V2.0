from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ver_paciente/<int:id>', views.ver_pacientes, name="ver_pacientes"),
    path('cadastrar_paciente', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('excluir_paciente/<int:id>',
         views.excluir_paciente, name="excluir_paciente"),
    path('alterar_paciente', views.alterar_paciente, name="alterar_paciente")
]

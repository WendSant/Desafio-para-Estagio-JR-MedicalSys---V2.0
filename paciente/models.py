from datetime import date
from pyexpat import model
from django.db import models

from medico.models import Medicos


class Pacientes(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    territorio = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)
    data_criacao = models.DateField(default=date.today)
    medico = models.ForeignKey(Medicos, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Paciente"

    def __str__(self) -> str:
        return self.nome

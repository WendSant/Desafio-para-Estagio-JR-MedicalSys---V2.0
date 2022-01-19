from datetime import date
from django.db import models


class Pacientes(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    territorio = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)
    data_criacao = models.DateField(default=date.today)

    class Meta:
        verbose_name = "Paciente"

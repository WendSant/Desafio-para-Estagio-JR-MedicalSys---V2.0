from datetime import date
from pyexpat import model
from django.db import models
from django.core.validators import RegexValidator
from medico.models import Medicos

my_validator = RegexValidator(
    "\d{6}\-\d{2}", "CAPA format needs to be ######-##.")


class Pacientes(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(
        max_length=10, validators=[my_validator])
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=20)
    territorio = models.CharField(max_length=20, default="Brasil")
    data_criacao = models.DateField(default=date.today)
    medico = models.ForeignKey(Medicos, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Paciente"

    def __str__(self) -> str:
        return self.nome

from datetime import date
from tabnanny import verbose
from this import d
from django.db import models

# Create your models here.


class Medicos(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=100)
    data_criacao = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name = "Medico"

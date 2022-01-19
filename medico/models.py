from tabnanny import verbose
from this import d
from django.db import models

# Create your models here.

class Medicos(models.Model):
   nome = models.CharField(max_length= 50) 
   email = models.CharField(max_length= 100)
   senha = models.CharField(max_length=100)
   data_criacao = models.DateTimeField()

   class Meta:
       verbose_name = "Medico"
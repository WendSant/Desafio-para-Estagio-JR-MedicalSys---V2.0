from dataclasses import fields
from django import forms
from .models import Pacientes


class CadastroPaciente(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'

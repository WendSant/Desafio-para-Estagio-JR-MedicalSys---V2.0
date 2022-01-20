from dataclasses import fields
from django import forms
from .models import Pacientes


class CadastroPaciente(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medico'].widget = forms.HiddenInput()
        self.fields['data_criacao'].widget = forms.HiddenInput()

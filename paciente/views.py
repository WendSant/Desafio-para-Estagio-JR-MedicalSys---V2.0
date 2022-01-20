from django.shortcuts import redirect, render
from django.http import HttpResponse
from medico.models import Medicos
from .models import Medicos, Pacientes


def home(request):
    if request.session.get('medico'):
        medico = Medicos.objects.get(id=request.session['medico'])
        pacientes = Pacientes.objects.filter(medico=medico)
        return render(request, 'home.html', {'pacientes': pacientes})
    else:
        return redirect('/auth/login/?status=2')


def ver_pacientes(request, id):
    pacientes = Pacientes.objects.get(id=id)
    print(pacientes)
    return render(request, 'ver_paciente.html', {'paciente': pacientes})

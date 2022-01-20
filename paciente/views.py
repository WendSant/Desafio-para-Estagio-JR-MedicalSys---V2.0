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
    if request.session.get('medico'):
        pacientes = Pacientes.objects.get(id=id)
        if request.session.get('medico') == pacientes.medico.id:
            medico_atual = Medicos.objects.all()
            print(medico_atual)
            return render(request, 'ver_paciente.html', {'paciente': pacientes, 'medico_atual': medico_atual})
        else:
            return HttpResponse('Paciente não pertence a este medico')
    return redirect('/auth/login/?status=2')

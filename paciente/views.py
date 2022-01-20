from django.shortcuts import redirect, render
from django.http import HttpResponse
from medico.models import Medicos
from .models import Medicos, Pacientes
from .forms import CadastroPaciente


def home(request):
    if request.session.get('medico'):
        medico = Medicos.objects.get(id=request.session['medico'])
        pacientes = Pacientes.objects.filter(medico=medico)
        form = CadastroPaciente()
        return render(request, 'home.html', {'pacientes': pacientes, 'medico_logado': request.session.get('medico'), 'form': form})
    else:
        return redirect('/auth/login/?status=2')


def ver_pacientes(request, id):
    if request.session.get('medico'):
        pacientes = Pacientes.objects.get(id=id)
        if request.session.get('medico') == pacientes.medico.id:
            medico_atual = Medicos.objects.all()
            form = CadastroPaciente()

            return render(request, 'ver_paciente.html', {'paciente': pacientes, 'medico_atual': medico_atual, 'medico_logado': request.session.get('medico'), 'form': form})
        else:
            return HttpResponse('Paciente não pertence a este medico')
    return redirect('/auth/login/?status=2')


def cadastrar_paciente(request):
    if request.method == 'POST':
        form = CadastroPaciente(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('SALVADO')
        else:
            return HttpResponse('DADOS INVALIDOS')

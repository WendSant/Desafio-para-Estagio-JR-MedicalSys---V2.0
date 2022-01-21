from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from medico.models import Medicos
from .models import Medicos, Pacientes
from .forms import CadastroPaciente


def home(request):
    if request.session.get('medico'):
        medico = Medicos.objects.get(id=request.session['medico'])
        cadastro_paciente = request.GET.get('cadastro_paciente')
        pacientes = Pacientes.objects.filter(medico=medico)
        form = CadastroPaciente()
        form.fields['medico'].initial = request.session['medico']
        return render(request, 'home.html', {'pacientes': pacientes, 'medico_logado': request.session.get('medico'), 'form': form, 'cadastro_paciente': cadastro_paciente})
    else:
        return redirect('/auth/login/?status=2')


def ver_pacientes(request, id):
    if request.session.get('medico'):
        pacientes = Pacientes.objects.get(id=id)
        if request.session.get('medico') == pacientes.medico.id:

            medico_atual = Medicos.objects.all()
            form = CadastroPaciente()
            form.fields['medico'].initial = request.session['medico']
            form.fields['data_criacao'].initial = request.session['medico']
            return render(request, 'ver_paciente.html', {'paciente': pacientes, 'medico_atual': medico_atual, 'medico_logado': request.session.get('medico'), 'form': form, 'id_paciente': id})
        else:
            return redirect('/paciente/home/?cadastro_paciente=2')
    return redirect('/auth/login/?status=2')


def cadastrar_paciente(request):
    if request.method == 'POST':
        form = CadastroPaciente(request.POST)
        if int(request.POST.get('medico')) == int(request.session.get('medico')):
            print(request.POST.get('medico'))
            if form.is_valid():
                form.save()
                return redirect('/paciente/home')
            else:
                return redirect('/paciente/home/?cadastro_paciente=1')
        else:
            return redirect('/paciente/home/?cadastro_paciente=1')
    else:
        return redirect('/paciente/home/?cadastro_paciente=1')


def excluir_paciente(request, id):
    if request.session.get('medico'):
        pacientes = Pacientes.objects.get(id=id)
        if request.session.get('medico') == pacientes.medico.id:
            paciente = Pacientes.objects.get(id=id).delete()
            return redirect('/paciente/home/')
        else:
            return redirect('/paciente/home/?cadastro_paciente=2')
    else:
        return redirect('/auth/login/?status=2')


def alterar_paciente(request):
    paciente_id = request.POST.get('paciente_id')
    paciente_nome = request.POST.get('paciente_nome')
    paciente_telefone = request.POST.get('paciente_telefone')
    paciente_cep = request.POST.get('paciente_cep')
    paciente_endereco = request.POST.get('paciente_endereco')
    paciente_estado = request.POST.get('paciente_estado')
    paciente_cidade = request.POST.get('paciente_cidade')
    paciente_territorio = request.POST.get('paciente_territorio')
    paciente = get_object_or_404(Pacientes, id=paciente_id)

    if paciente.medico.id == request.session['medico']:
        paciente.nome = paciente_nome
        paciente.telefone = paciente_telefone
        paciente.cep = paciente_cep
        paciente.endereco = paciente_endereco
        paciente.estado = paciente_estado
        paciente.cidade = paciente_cidade
        paciente.territorio = paciente_territorio
        paciente.save()
        return redirect(f'/paciente/ver_paciente/{paciente_id}')
    else:
        return redirect('/auth/sair')

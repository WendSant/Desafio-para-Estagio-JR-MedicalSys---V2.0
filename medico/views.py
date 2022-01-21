from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Medicos
from paciente.models import Pacientes
from paciente.views import excluir_paciente


def login(request):
    if request.session.get('medico'):
        return redirect('/paciente/home/')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastrar(request):
    if request.session.get('medico'):
        return redirect('/paciente/home/')
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    medico = Medicos.objects.filter(email=email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastrar/?status=1')

    if len(senha) < 8:
        return redirect('/auth/cadastrar/?status=2')

    if len(medico) > 0:
        return redirect('/auth/cadastrar/?status=3')
    try:
        medico = Medicos(nome=nome, senha=senha, email=email)
        medico.save()

        return redirect('/auth/cadastrar/?status=0')
    except:
        return redirect('/auth/cadastrar/?status=4')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    medico = Medicos.objects.filter(email=email).filter(senha=senha)

    if len(medico) == 0:
        return redirect('/auth/login/?status=1')
    elif len(medico) > 0:
        request.session['medico'] = medico[0].id
        return redirect('/paciente/home')

    return HttpResponse(f'{email} {senha}')


def home_medico(request):
    medicos = Medicos.objects.all()
    medico_excluido = request.GET.get('medico_excluido')
    return render(request, 'home_medico.html', {'medicos': medicos, 'medico_excluido': medico_excluido})


def ver_medicos(request, id):
    medicos = Medicos.objects.get(id=id)

    return render(request, 'ver_medico.html', {'medico': medicos, 'id_medico': id})


def sair(request):
    request.session.flush()
    return redirect('/auth/login')


def excluir_medico(request, id):
    medicos = Medicos.objects.get(id=id)
    Pacientes.objects.filter(medico=medicos).delete()
    medico = Medicos.objects.get(id=id).delete()
    return redirect('/auth/home_medico/?medico_excluido=1')


def alterar_medico(request):
    medico_id = request.POST.get('medico_id')
    medico = get_object_or_404(Medicos, id=medico_id)
    medico.nome = request.POST.get('medico_nome')
    medico.email = request.POST.get('medico_email')
    medico.senha = request.POST.get('medico_senha')
    medico.save()
    return redirect(f'/auth/ver_medico/{medico_id}')

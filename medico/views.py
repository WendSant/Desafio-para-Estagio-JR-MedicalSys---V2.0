from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Medicos


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


def sair(request):
    request.session.flush()
    return redirect('/auth/login')

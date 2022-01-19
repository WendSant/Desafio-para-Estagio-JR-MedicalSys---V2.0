from django.shortcuts import redirect, render
from django.http import HttpResponse
from medico.models import Medicos


def home(request):
    if request.session.get('medico'):
        medico = Medicos.objects.get(id=request.session['medico']).nome
        return HttpResponse(f'Hiii {medico}')
    else:
        return redirect('/auth/login/?status=2')

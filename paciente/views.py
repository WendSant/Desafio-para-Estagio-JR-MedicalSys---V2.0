from django.shortcuts import redirect, render
from django.http import HttpResponse


def home(request):
    if request.session.get('medico'):
        return HttpResponse('Hiii')
    else:
        return redirect('/auth/login/?status=2')

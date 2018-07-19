# coding: utf-8
from django.shortcuts import render, get_object_or_404
from web1.forms import *
from django.shortcuts import redirect
from web1.models.permissao_model import Permissao

def login_verifica_grupo(request):
    if request.user.is_authenticated():
        if request.user.groups.all():
            if request.user.groups.get().name == "Nupe":
                return render(request, 'web1/funcionario_nupe.html', {'grupo_user': 'nupe'})

            if request.user.groups.get().name == "Portaria":
                permissoes = Permissao.objects.all().order_by('data').exclude(excluido=True).exclude(aluno__excluido=True)
                return render(request, 'web1/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'portaria'})

            if request.user.groups.get().name == "Professor":
                permissoes = Permissao.objects.all().order_by('data').exclude(excluido=True).exclude(aluno__excluido=True)
                return render(request, 'web1/permissaoLista.html',
                              {'permissoes': permissoes, 'grupo_user': 'professor'})
    else:
        return redirect('/accounts/login/')
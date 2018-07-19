# coding: utf-8
from django.shortcuts import render, get_object_or_404
from web1.forms import *
from django.views.generic.base import View
from web1.models.permissao_model import Permissao
from web1.models.funcionario_model import Funcionario


class ValidaPermissaoProfessorView(View):
    template = 'web1/permissaoLista.html'
    def get(self, request, id=None):
        permissao = Permissao.objects.get(pk=id)
        permissao.verificado_professor = Funcionario.objects.get(pessoa_funcionario=request.user.id)
        permissao.save()
        permissoes = Permissao.objects.all().exclude(excluido=True).exclude(aluno__excluido=True)
        return render(request, self.template, {'permissoes': permissoes, 'grupo_user': 'professor'})


class ValidaPermissaoPortariaView(View):
    template = 'web1/permissaoLista.html'
    def get(self, request, id=None):
        permissao = Permissao.objects.get(pk=id)
        permissao.verificado_portaria = Funcionario.objects.get(pessoa_funcionario=request.user.id)
        permissao.save()
        permissoes = Permissao.objects.all().exclude(excluido=True).exclude(aluno__excluido=True)
        return render(request, self.template, {'permissoes': permissoes, 'grupo_user': 'portaria'})
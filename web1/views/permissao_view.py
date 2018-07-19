# coding: utf-8
from django.shortcuts import render, get_object_or_404
from datetime import date
from web1.forms import *
from django.views.generic.base import View
from web1.models.aluno_model import Aluno
from web1.models.permissao_model import Permissao
from web1.forms.permissao_form import PermissaoForm
from web1.models.funcionario_model import Funcionario

class CadastraPermissaoView(View):
    template = 'web1/permissaoAdd.html'

    def get(self, request, id=None):
        form = PermissaoForm()
        aluno = Aluno.objects.get(pk=id)
        return render(request, self.template, {'form': form, 'grupo_user': 'nupe', 'aluno': aluno})

    def post(self, request, id=None):
        aluno = []
        form = PermissaoForm(request.POST)
        if form.is_valid():
            permissao = form.save(commit=False)
            funcionario = Funcionario.objects.get(pessoa_funcionario=request.user.id)
            permissao.funcionario_nupe = funcionario
            permissao.data = date.today()
            permissao.save()
            msg = "Permissão cadastrada com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
        return render(request, self.template, {'form': form, 'grupo_user': 'nupe', 'aluno': aluno})

class EditaPermissaoView(View):
    template_edit_permissao = 'web1/permissaoAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request, id, id_aluno):
        permissao = Permissao.objects.get(pk=id)
        aluno = Aluno.objects.get(pk=id_aluno)
        form = PermissaoForm(instance=permissao)
        return render(request, self.template_edit_permissao, {'form': form, 'grupo_user': 'nupe', 'permissao': permissao, 'aluno': aluno})

    def post(self, request, id, id_aluno):
        aluno = Aluno.objects.get(pk=id_aluno)
        permissao = Permissao.objects.get(pk=id)
        form = PermissaoForm(request.POST, instance=permissao)
        if form.is_valid():
            permissao = form.save(commit=False)
            funcionario = Funcionario.objects.get(pessoa_funcionario=request.user.id)
            permissao.funcionario_nupe = funcionario
            permissao.data = date.today()
            permissao.save()
            msg = "Permissão editada com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
            return render(request, self.template_edit_permissao,
                          {'form': form, 'grupo_user': 'nupe', 'permissao': permissao, 'aluno': aluno})
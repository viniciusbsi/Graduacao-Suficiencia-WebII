# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from web1.forms import *
from django.contrib.auth.models import Group, User
from django.views.generic.base import View
from web1.forms.funcionario_form import FuncionarioForm
from web1.forms.pessoa_form import PessoaForm
from web1.forms.pessoa_password_form import PessoaPasswordForm
from web1.models.funcionario_model import Funcionario

class CadastraFuncionarioView(View):
    template = 'web1/funcionarioAdd.html'

    def get(self, request):
        form = FuncionarioForm()
        form_pessoa = PessoaForm()
        form_senha = PessoaPasswordForm()
        return render(request, self.template,{'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha, 'grupo_user': 'nupe'})

    def post(self, request):
        form = FuncionarioForm(request.POST)
        form_pessoa = PessoaForm(request.POST)
        form_senha = PessoaPasswordForm(request.POST)
        if form.is_valid() and form_pessoa.is_valid() and form_senha.is_valid():
            obj_pessoa = form_pessoa.save(commit=False)
            grupo = Group.objects.get(pk=request.POST['groups'])
            obj_pessoa.save()
            obj_pessoa.groups.add(grupo)
            user = User.objects.last()
            user.set_password(request.POST['password'])
            user.save()
            obj = form.save(commit=False)
            obj.pessoa_funcionario = User.objects.last()
            obj.save()
            msg = "Funcionário cadastrado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})

        else:
            print(form_pessoa.errors)
            print(form_senha.errors)
            print(form.errors)
            return render(request, self.template, {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha, 'grupo_user': 'nupe'})


class EditaFuncionarioView(View):
    template_edit_funcionario = 'web1/funcionarioAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request, id):
        funcionario = Funcionario.objects.get(pk=id)
        form = FuncionarioForm(instance=funcionario)
        form_pessoa = PessoaForm(instance=funcionario.pessoa_funcionario)
        form_senha = PessoaPasswordForm()
        return render(request, self.template_edit_funcionario,
                      {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha, 'grupo_user': 'nupe',
                       'funcionario': funcionario})

    def post(self, request, id):
        funcionario = Funcionario.objects.get(pk=id)
        form = FuncionarioForm(request.POST, instance=funcionario)
        form_pessoa = PessoaForm(request.POST, instance=funcionario.pessoa_funcionario)
        form_senha = PessoaPasswordForm(request.POST)
        if form.is_valid() and form_pessoa.is_valid() and form_senha.is_valid():
            obj_pessoa = form_pessoa.save(commit=False)
            grupo = Group.objects.get(pk=request.POST['groups'])
            obj_pessoa.save()
            obj_pessoa.groups.add(grupo)
            user = User.objects.last()
            user.set_password(request.POST['password'])
            user.save()
            obj = form.save(commit=False)
            obj.pessoa_funcionario = User.objects.last()
            obj.save()
            msg = "Funcionário editado com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})

        else:
            print(form_pessoa.errors)
            print(form_senha.errors)
            print(form.errors)
            return render(request, self.template_edit_funcionario,
                          {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha, 'grupo_user': 'nupe',
                           'funcionario': funcionario})




# coding: utf-8
from django.shortcuts import render, get_object_or_404
from web1.forms.aluno_form import AlunoForm
from django.views.generic.base import View
from django.db.models import Q
from web1.models.aluno_model import Aluno


class CadastroAlunoView(View):
    def get(self, request):
        form = AlunoForm()
        return render(request, 'web1/alunoAdd.html', {'form': form, 'grupo_user': 'nupe'})

    def post(self, request):
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Aluno cadastrado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})

        else:
            print (form.errors)
            return render(request, 'web1/alunoAdd.html', {'form': form, 'grupo_user': 'nupe'})

class EdicaoAlunoView(View):
    template_cad_aluno = 'web1/alunoAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'
    def get(self, request, id=None):
        aluno = Aluno.objects.get(pk=id)
        form = AlunoForm(instance=aluno)
        return render(request, self.template_cad_aluno, {'form': form, 'grupo_user': 'nupe', 'aluno': aluno})

    def post(self, request, id=None):
        aluno = Aluno.objects.get(pk=id)
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            msg = "Aluno editado com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})

        else:
            print (form.errors)
            return render(request, self.template_cad_aluno, {'form': form, 'grupo_user': 'nupe', 'aluno': aluno})

class ListaAlunoView(View):
    template = 'web1/selecionaAlunoPermissao.html'
    def get(self, request):
        if 'filtro_aluno' in request.GET:

            alunos = Aluno.objects.filter(Q(nome__icontains=request.GET.get('filtro_aluno'))|
                Q(curso__nome__icontains=request.GET.get('filtro_aluno'))|
                Q(matricula__icontains=request.GET.get('filtro_aluno'))|
                Q(turma__nome__icontains=request.GET.get('filtro_aluno'))).exclude(excluido=True).distinct()
        else:
            alunos = Aluno.objects.all().exclude(excluido=True)

        return render(request, self.template, {'alunos': alunos, 'grupo_user': 'nupe'})

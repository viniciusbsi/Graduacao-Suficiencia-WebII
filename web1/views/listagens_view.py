# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from web1.forms import *
from django.db.models import Q
from django.views.generic.base import View
from web1.models import *


class AlunoList(ListView):
    queryset = Aluno.objects.all().exclude(excluido=True)
    template_name = 'web1/alunosLista.html'

class FuncionarioList(ListView):
    context_object_name = 'object_list'
    queryset = Funcionario.objects.all().exclude(excluido=True)
    template_name = 'web1/funcionariosLista.html'

class CursoList(ListView):
    queryset = Curso.objects.all().exclude(excluido=True)
    template_name = 'web1/cursosLista.html'

class TurmaList(ListView):
    queryset = Turma.objects.all().exclude(excluido=True)
    template_name = 'web1/turmasLista.html'

class PermissoesListaView(View):
    template = 'web1/permissaoLista.html'
    def get(self, request):
        if 'filtro' in request.GET:
            permissoes = Permissao.objects.filter(Q(aluno__nome__icontains=request.GET.get('filtro'))|
                Q(aluno__curso__descricao__icontains=request.GET.get('filtro'))|
                Q(aluno__turma__descricao__icontains=request.GET.get('filtro'))).exclude(excluido=True).exclude(aluno__excluido=True)
        else:
            permissoes = Permissao.objects.all().order_by('data').exclude(excluido=True).exclude(aluno__excluido=True)
        return render(request, self.template, {'permissoes': permissoes, 'grupo_user': 'nupe'})











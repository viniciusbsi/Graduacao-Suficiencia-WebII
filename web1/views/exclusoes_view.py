# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from web1.models import *

@login_required
def exclui_aluno(request, id):
    obj = Aluno.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Aluno removido com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_funcionario(request, id):
    obj = Funcionario.objects.get(pk=id)
    obj.excluido = True
    obj.pessoa_funcionario.is_active = False
    obj.pessoa_funcionario.save()
    obj.save()
    msg = "Funcionário removido com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_permissao(request, id):
    obj = Permissao.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Permissao removida com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_curso(request, id):
    obj = Curso.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Curso removido com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_turma(request, id):
    obj = Turma.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Turma removida com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

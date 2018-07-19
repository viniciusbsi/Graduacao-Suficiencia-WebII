# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from web1.forms import *
from django.views.generic.base import View
from web1.models.turma_model import Turma
from web1.forms.turma_form import TurmaForm

class CadastraTurmaView(View):
    template_cad_turma = 'web1/turmaAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request):
        form = TurmaForm()
        return render(request, self.template_cad_turma, {'form': form, 'grupo_user': 'nupe'})

    def post(self, request):
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Turma cadastrada com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
            return render(request, self.template_cad_turma, {'form': form, 'grupo_user': 'nupe'})


class EditaTurmaView(View):
    template_edit_turma = 'web1/turmaAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request, id=None):
        turma = Turma.objects.get(pk=id)
        form = TurmaForm(instance=turma)
        return render(request, self.template_edit_turma, {'form': form, 'grupo_user': 'nupe', 'turma': turma})

    def post(self, request, id=None):
        turma = Turma.objects.get(pk=id)
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            msg = "Turma editada com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
            return render(request, self.template_edit_turma, {'form': form, 'grupo_user': 'nupe', 'turma': turma})

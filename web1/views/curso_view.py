# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from web1.forms.curso_form import CursoForm
from web1.models.curso_model import Curso
from django.views.generic.base import View

class CadastraCursoView(View):
    template_cad_curso = 'web1/cursoAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request):
        form = CursoForm()
        return render(request, self.template_cad_curso, {'form': form, 'grupo_user': 'nupe'})

    def post(self, request):
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Curso cadastrado com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
            return render(request, self.template_cad_curso, {'form': form, 'grupo_user': 'nupe'})


class EditaCursoView(View):
    template_edit_curso = 'web1/cursoAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request):
        curso = Curso.objects.get(pk=id)
        form = CursoForm(instance=curso)
        return render(request, self.template_edit_curso , {'form': form, 'grupo_user': 'nupe', 'curso': curso})

    def post(self, request, id=None):
        curso = Curso.objects.get(pk=id)
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            msg = "Curso editado com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
            return render(request, self.template_edit_curso , {'form': form, 'grupo_user': 'nupe', 'curso': curso})

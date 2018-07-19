# coding: utf-8
from django.shortcuts import render, get_object_or_404
from web1.forms import *
from django.views.generic.base import View
from web1.forms.tipo_permissao_form import TipoPermissaoForm


class CadastraTipoPermissaoView(View):
    template_cad_tipo_permissao = 'web1/tipoPermissaoAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request):
        form = TipoPermissaoForm()
        return render(request, self.template_cad_tipo_permissao, {'form': form, 'grupo_user': 'nupe'})

    def post(self, request):
        form = TipoPermissaoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Tipo de permissão cadastrada com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
            return render(request, self.template_cad_tipo_permissao, {'form': form, 'grupo_user': 'nupe'})

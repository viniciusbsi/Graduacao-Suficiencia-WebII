# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from web1.forms import *
from django.views.generic.base import View
from web1.forms.tipo_oferta_form import TipoOfertaForm


class CadastraTipoOfertaView(View):
    template_cad_tipo_oferta = 'web1/tipoOfertaAdd.html'
    template_home_nupe = 'web1/funcionario_nupe.html'

    def get(self, request):
        form = TipoOfertaForm()
        return render(request, self.template_cad_tipo_oferta, {'form': form, 'grupo_user': 'nupe'})

    def post(self, request):
        form = TipoOfertaForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Tipo de oferta cadastrada com sucesso!"
            return render(request, self.template_home_nupe, {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
            return render(request, self.template_cad_tipo_oferta, {'form': form, 'grupo_user': 'nupe'})

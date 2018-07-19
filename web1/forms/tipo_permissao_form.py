# coding: utf-8

from django import forms
from web1.models import *


class TipoPermissaoForm(forms.ModelForm):
    class Meta:
        model = TipoPermissao
        fields = '__all__'

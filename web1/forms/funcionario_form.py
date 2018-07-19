# coding: utf-8

from django import forms
from web1.models import *


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        exclude = ['pessoa_funcionario']
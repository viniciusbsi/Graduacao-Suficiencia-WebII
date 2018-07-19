# coding: utf-8

from django import forms
from web1.models import *


class PermissaoForm(forms.ModelForm):
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all().exclude(excluido=True),
                                   widget=forms.Select(attrs={'placeholder': 'Selecione o segurado',
                                                              "class": "ui fluid search selection dropdown"}))

    class Meta:
        model = Permissao
        fields = '__all__'
        exclude = ['funcionario_nupe', 'data']
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
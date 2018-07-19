# coding: utf-8

from django import forms
from web1.models import *


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
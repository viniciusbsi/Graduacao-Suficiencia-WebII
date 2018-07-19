# coding: utf-8

from django import forms
from web1.models import *


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }

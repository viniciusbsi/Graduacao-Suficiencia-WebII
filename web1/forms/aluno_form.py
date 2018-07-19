# coding: utf-8

from django import forms
from web1.models import *

class AlunoForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all().exclude(excluido=True))
    turma = forms.ModelChoiceField(queryset=Turma.objects.all().exclude(excluido=True))

    class Meta:
        model = Aluno
        fields = '__all__'
        exclude = ['pessoa_aluno']
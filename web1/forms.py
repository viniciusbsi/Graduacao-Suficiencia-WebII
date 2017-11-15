# coding: utf-8

from django import forms
from .models import *
from django.contrib.auth.models import User
from validacoes import ValidarPassword, ValidarTamanhoPassword
from django.contrib.auth.models import Group

class PermissaoForm(forms.ModelForm):

    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all().exclude(excluido=True),
                                   widget=forms.Select(attrs={'placeholder': 'Selecione o segurado',
                                                                 "class": "ui fluid search selection dropdown"}))
    class Meta:
        model = Permissao
        fields = '__all__'
        exclude = ['funcionario_nupe', 'data']

class TurmaForm(forms.ModelForm):

    class Meta:
        model = Turma
        fields = '__all__'

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'

class TipoPermissaoForm(forms.ModelForm):

    class Meta:
        model = TipoPermissao
        fields = '__all__'

class TipoOfertaForm(forms.ModelForm):

    class Meta:
        model = TipoOferta
        fields = '__all__'

class AlunoForm(forms.ModelForm):

    matricula = forms.CharField(max_length=20)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all().exclude(excluido=True))
    turma = forms.ModelChoiceField(queryset=Turma.objects.all().exclude(excluido=True))
    class Meta:
        model = Aluno
        fields = '__all__'
        exclude = ['pessoa_aluno']


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        exclude = ['pessoa_funcionario']


class PessoaForm(forms.ModelForm):

    groups = forms.ModelChoiceField(queryset=Group.objects.all().exclude(name='Aluno'), required=True)

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'user_permissions', 'is_active', 'date_joined', 'is_staff', 'password']

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        # self.fields['groups'].required = True
        # self.fields['groups'].widget = forms.SelectMultiple(
        #             choices=Group.objects.all().exclude(name='Aluno').values_list('id', 'name'),
        #             attrs={'class': 'ui dropdown'})

    def clean_groups(self):

        if not self.cleaned_data['groups']:
            raise forms.ValidationError("Escolha uma função")
        else:
            return self.cleaned_data['groups']

class AlunoPessoaForm(forms.ModelForm):

    # username = forms.CharField(required=False)
    # groups = forms.ModelChoiceField(queryset=Group.objects.all().exclude(name='Aluno'), required=True)

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'user_permissions', 'is_active', 'date_joined', 'is_staff', 'password']


class PessoaPasswordForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    password_checker = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['password']

    def clean_password(self):
        return ValidarTamanhoPassword(self.cleaned_data['password'])

    def clean_password_checker(self):
        return ValidarPassword(self.cleaned_data.get('password'), self.cleaned_data.get('password_checker'))

    # def save(self, commit=True):
    #     user = super(PessoaPasswordForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     if commit:
    #         user.save()
from django import forms
from .models import *
from django.contrib.auth.models import User
from validacoes import ValidarPassword, ValidarTamanhoPassword
from django.contrib.auth.models import Group

class PermissaoForm(forms.ModelForm):

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

# class FuncaoForm(forms.ModelForm):
#
#     class Meta:
#         model = Funcao
#         fields = '__all__'

class AlunoForm(forms.ModelForm):

    matricula = forms.IntegerField(required=True)

    class Meta:
        model = Aluno
        fields = '__all__'
        exclude = ['pessoa_aluno']


class FuncionarioForm(forms.ModelForm):

    matricula = forms.IntegerField(required=False)

    class Meta:
        model = Funcionario
        fields = '__all__'
        exclude = ['pessoa_funcionario']


class PessoaForm(forms.ModelForm):

        # groups = forms.ModelChoiceField(required=False,
        #                                 empty_label='Selecione o grupo',
        #                                 queryset=Group.objects.all(),
        #                                 widget=forms.Select(attrs={"class": "ui fluid search selection dropdown", })
        #                                 )

    class Meta:
        model = User
        fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'user_permissions', 'is_active', 'date_joined', 'is_staff', 'password']


class PessoaPasswordForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput())
    password_checker = forms.CharField(required=False, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['password']

    def clean_password(self):
        return ValidarTamanhoPassword(self.cleaned_data['password'])

    def clean_password_checker(self):
        return ValidarPassword(self.cleaned_data.get('password'), self.cleaned_data.get('password_checker'))

    def save(self, commit=True):
        user = super(PessoaPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
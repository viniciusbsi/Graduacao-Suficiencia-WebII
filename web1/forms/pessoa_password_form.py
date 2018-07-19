# coding: utf-8

from django import forms
from web1.models import *
from django.contrib.auth.models import User
from web1.views.validacoes import ValidarTamanhoPassword, ValidarPassword
from django.contrib.auth.models import Group



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

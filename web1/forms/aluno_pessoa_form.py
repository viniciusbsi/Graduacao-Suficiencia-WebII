# coding: utf-8
from django import forms
from django.contrib.auth.models import User


class AlunoPessoaForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'user_permissions', 'is_active', 'date_joined', 'is_staff', 'password']
# coding: utf-8
from django import forms


def ValidarPassword(password, password_checker):
    if password != password_checker:
        raise forms.ValidationError("Senhas diferentes")
    else:
        return password_checker


def ValidarTamanhoPassword(senha):
    if len(senha) >= 6:
        return senha
    else:
        raise forms.ValidationError("A senha deve conter no mínimo 6 caracteres")
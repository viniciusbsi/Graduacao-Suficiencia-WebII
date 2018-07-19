# coding: utf-8

from django import forms
from web1.models import *


class TipoOfertaForm(forms.ModelForm):
    class Meta:
        model = TipoOferta
        fields = '__all__'

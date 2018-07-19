# coding: utf-8

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


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

    def clean_groups(self):

        if not self.cleaned_data['groups']:
            raise forms.ValidationError("Escolha uma função")
        else:
            return self.cleaned_data['groups']

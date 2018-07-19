# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator

class Funcionario(models.Model):
    pessoa_funcionario = models.ForeignKey('auth.User')
    matricula = models.IntegerField(validators=[MinValueValidator(0)])
    # funcao = models.ForeignKey('web1.Funcao', related_name='Funcionario_Funcao')
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.pessoa_funcionario.get_full_name()

    def __str__(self):
        return self.pessoa_funcionario.get_full_name()
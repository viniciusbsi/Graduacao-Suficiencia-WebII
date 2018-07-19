# coding: utf-8

from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=500)
    ano = models.CharField(max_length=5)
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome
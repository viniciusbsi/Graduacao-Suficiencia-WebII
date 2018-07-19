# coding: utf-8
from django.db import models
from django.core.validators import MinValueValidator


class Aluno(models.Model):
    matricula = models.IntegerField(validators=[MinValueValidator(0)])
    nome = models.CharField(max_length=200)
    nome_pai = models.CharField(max_length=200, null=True, blank=True)
    nome_mae = models.CharField(max_length=200)
    email = models.EmailField()
    telefone_aluno = models.CharField(max_length=16, null=True, blank=True)
    telefone_responsavel = models.CharField(max_length=16)
    curso = models.ForeignKey('web1.Curso', related_name='Aluno_Curso')
    turma = models.ForeignKey('web1.Turma', related_name='Aluno_turma')
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s'%self.nome

    def __str__(self):
        return '%s'%self.nome
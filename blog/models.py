# coding: utf-8

from django.db import models


class Aluno(models.Model):
    matricula = models.PositiveIntegerField()
    nome = models.CharField(max_length=200)
    nome_pai = models.CharField(max_length=200, null=True, blank=True)
    nome_mae = models.CharField(max_length=200)
    email = models.EmailField()
    telefone_aluno = models.CharField(max_length=16, null=True, blank=True)
    telefone_responsavel = models.CharField(max_length=16)
    curso = models.ForeignKey('blog.Curso', related_name='Aluno_Curso')
    turma = models.ForeignKey('blog.Turma', related_name='Aluno_turma')

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Permissao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    hora_solicitada = models.TimeField()
    funcionario_nupe = models.ForeignKey('blog.Funcionario', related_name='Permissao_FuncionarioNupe')
    aluno = models.ForeignKey('blog.Aluno', related_name='Permissao_Aluno')
    verificado_professor = models.ForeignKey('blog.Funcionario', related_name='Permissao_Valida_Professor', blank=True, null=True)
    verificado_portaria = models.ForeignKey('blog.Funcionario', related_name='Permissao_Valida_Portaria', blank=True, null=True)

    def __unicode__(self):
        return self.aluno

    def __str__(self):
        return self.aluno


class Funcionario(models.Model):
    pessoa_funcionario = models.ForeignKey('auth.User')
    matricula = models.PositiveIntegerField(blank=False)
    # funcao = models.ForeignKey('blog.Funcao', related_name='Funcionario_Funcao')

    def __unicode__(self):
        return self.pessoa_funcionario.get_full_name()

    def __str__(self):
        return self.pessoa_funcionario.get_full_name()


class Funcao(models.Model):
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Curso(models.Model):
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Turma(models.Model):
    descricao = models.CharField(max_length=200)
    ano = models.CharField(max_length=5)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao
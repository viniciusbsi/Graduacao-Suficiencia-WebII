# coding: utf-8

from django.db import models
from django.core.validators import MinValueValidator



class Aluno(models.Model):
    matricula = models.IntegerField(validators=[MinValueValidator(0)], max_length=20)
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
        return self.nome

    def __str__(self):
        return self.nome


class Permissao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=50)
    hora_solicitada = models.TimeField()
    funcionario_nupe = models.ForeignKey('web1.Funcionario', related_name='Permissao_FuncionarioNupe')
    aluno = models.ForeignKey('web1.Aluno', related_name='Permissao_Aluno')
    verificado_professor = models.ForeignKey('web1.Funcionario', related_name='Permissao_Valida_Professor', blank=True, null=True)
    verificado_portaria = models.ForeignKey('web1.Funcionario', related_name='Permissao_Valida_Portaria', blank=True, null=True)
    tipo_permissao = models.ForeignKey('web1.TipoPermissao', related_name='Permissao_Tipo_Permissao')
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.aluno

    def __str__(self):
        return self.aluno


class Funcionario(models.Model):
    pessoa_funcionario = models.ForeignKey('auth.User')
    matricula = models.PositiveIntegerField(blank=False)
    # funcao = models.ForeignKey('web1.Funcao', related_name='Funcionario_Funcao')
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.pessoa_funcionario.get_full_name()

    def __str__(self):
        return self.pessoa_funcionario.get_full_name()


class Funcao(models.Model):
    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

class TipoPermissao(models.Model):
    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

class Curso(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    duracao = models.CharField(max_length=20)
    tipo_oferta = models.ForeignKey('web1.TipoOferta', related_name='Curso_Oferta')
    coordenador = models.CharField(max_length=200)
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class Turma(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.CharField(max_length=50)
    ano = models.CharField(max_length=5)
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao


class TipoOferta(models.Model):
    descricao = models.CharField(max_length=50)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao
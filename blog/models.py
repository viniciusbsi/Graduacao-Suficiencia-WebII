from django.db import models


class Aluno(models.Model):
    pessoa_aluno = models.ForeignKey('auth.User')
    matricula = models.IntegerField()
    nome_pai = models.CharField(max_length=200)
    nome_mae = models.CharField(max_length=200)
    telefone_aluno = models.CharField(max_length=16)
    telefone_responsavel = models.CharField(max_length=16)
    curso = models.ForeignKey('blog.Curso', related_name='Aluno_Curso')
    turma = models.ForeignKey('blog.Turma', related_name='Aluno_turma')

    def __unicode__(self):
        return self.pessoa_aluno.get_full_name()

    def __str__(self):
        return self.pessoa_aluno.get_full_name()


class Permissao(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    hora_solicitada = models.TimeField()
    funcionario_nupe = models.ForeignKey('blog.Funcionario', related_name='Permissao_FuncionarioNupe')
    aluno = models.ForeignKey('blog.Aluno', related_name='Permissao_Aluno')

    def __unicode__(self):
        return self.aluno

    def __str__(self):
        return self.aluno


class Funcionario(models.Model):
    pessoa_funcionario = models.ForeignKey('auth.User')
    matricula = models.IntegerField(blank=False)
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

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao
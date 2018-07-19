# coding: utf-8

from django.db import models

class Permissao(models.Model):
    data = models.DateField()
    descricao = models.TextField(max_length=500)
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
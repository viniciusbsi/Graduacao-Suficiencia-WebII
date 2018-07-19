# coding: utf-8

from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=500)
    duracao = models.CharField(max_length=20)
    tipo_oferta = models.ForeignKey('web1.TipoOferta', related_name='Curso_Oferta')
    coordenador = models.CharField(max_length=200)
    excluido = models.BooleanField(default=False)


    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

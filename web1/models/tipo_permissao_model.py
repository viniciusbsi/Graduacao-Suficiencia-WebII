# coding: utf-8

from django.db import models

class TipoPermissao(models.Model):
    descricao = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao
# coding=utf-8
"""Testes de models"""
from django.test import TestCase
from web1.models.turma_model import Turma


class TurmaModelTest(TestCase):
    """Classe de teste da model de turma"""
    def create_turma(self, turma=u'BSI Teste'):
        """Método que cria turma"""
        return Turma.objects.create(nome=turma)

    def test_turma_creation(self):
        """Método que testa a criação de turma"""
        turma = self.create_turma()
        self.assertTrue(isinstance(turma, Turma))
        self.assertEqual(turma.__unicode__(), turma.nome)

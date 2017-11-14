from django.conf.urls import patterns, include, url

from web1.views import AlunoList, FuncionarioList, TurmaList, CursoList
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login_verifica_grupo),
    url(r'^permissao/add/$', views.cadastra_permissao, name='cadastra_permissao'),
    url(r'^permissao/lista/$', views.lista_permissoes, name='lista_permissao'),
    url(r'^aluno/add/$', views.cadastra_aluno, name='cadastra_aluno'),
    url(r'^funcionario/add/$', views.cadastra_funcionario, name='cadastra_funcionario'),
    url(r'^permissao/valida/professor/(?P<id>\d+)/$', views.ValidaPermissaoProfessor, name='valida_permissao_professor'),
    url(r'^permissao/valida/portaria/(?P<id>\d+)/$', views.ValidaPermissaoPortaria, name='valida_permissao_professor'),
    url(r'^turma/add/$', views.cadastra_turma, name='cadastra_turma'),
    url(r'^curso/add/$', views.cadastra_curso, name='cadastra_curso'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
    url(r'^gera_comprovante/(?P<id>\d+)/$', views.GeraComprovantePDF, name='gera_comprovante'),
    url(r'^aluno/list/$', AlunoList.as_view(), name='aluno_list'),
    url(r'^funcionario/list/$', FuncionarioList.as_view(), name='funcionario_list'),
    url(r'^turma/list/$', TurmaList.as_view(), name='turma_list'),
    url(r'^curso/list/$', CursoList.as_view(), name='curso_list'),
]

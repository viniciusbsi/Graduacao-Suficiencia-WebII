from django.conf.urls import patterns, include, url

from web1.views import AlunoList, FuncionarioList, TurmaList, CursoList
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login_verifica_grupo),
    url(r'^permissao/add/$', views.cadastra_permissao, name='cadastra_permissao'),
    url(r'^permissao/edit/(?P<id>\d+)/$', views.edita_permissao, name='edita_permissao'),
    url(r'^tipo_permissao/add/$', views.cadastra_tipo_permissao, name='cadastra_tipo_permissao'),
    url(r'^tipo_oferta/add/$', views.cadastra_tipo_oferta, name='cadastra_tipo_oferta'),
    url(r'^permissao/lista/$', views.lista_permissoes, name='lista_permissao'),
    url(r'^aluno/add/$', views.cadastra_aluno, name='cadastra_aluno'),
    url(r'^aluno/edit/(?P<id>\d+)/$', views.edita_aluno, name='edita_aluno'),
    url(r'^funcionario/add/$', views.cadastra_funcionario, name='cadastra_funcionario'),
    url(r'^funcionario/edit/(?P<id>\d+)/$', views.edita_funcionario, name='edita_funcionario'),
    url(r'^permissao/valida/professor/(?P<id>\d+)/$', views.ValidaPermissaoProfessor, name='valida_permissao_professor'),
    url(r'^permissao/valida/portaria/(?P<id>\d+)/$', views.ValidaPermissaoPortaria, name='valida_permissao_professor'),
    url(r'^turma/add/$', views.cadastra_turma, name='cadastra_turma'),
    url(r'^turma/edit/(?P<id>\d+)/$', views.edita_turma, name='edita_turma'),
    url(r'^curso/add/$', views.cadastra_curso, name='cadastra_curso'),
    url(r'^curso/edit/(?P<id>\d+)/$', views.edita_curso, name='edita_curso'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
    url(r'^gera_comprovante/(?P<id>\d+)/$', views.GeraComprovantePDF, name='gera_comprovante'),
    url(r'^aluno/list/$', AlunoList.as_view(), name='aluno_list'),
    url(r'^funcionario/list/$', FuncionarioList.as_view(), name='funcionario_list'),
    url(r'^turma/list/$', TurmaList.as_view(), name='turma_list'),
    url(r'^curso/list/$', CursoList.as_view(), name='curso_list'),
    url(r'^remove/aluno/(?P<id>\d+)/$', views.exclui_aluno, name='exclui_aluno'),
    url(r'^remove/funcionario/(?P<id>\d+)/$', views.exclui_funcionario, name='exclui_funcionario'),
    url(r'^remove/permissao/(?P<id>\d+)/$', views.exclui_permissao, name='exclui_permissao'),
    url(r'^remove/turma/(?P<id>\d+)/$', views.exclui_turma, name='exclui_turma'),
    url(r'^remove/curso/(?P<id>\d+)/$', views.exclui_curso, name='exclui_curso'),
]

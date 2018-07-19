from django.conf.urls import patterns, include, url
from web1.views import *
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login_verifica_grupo, name='verifica_grupo'),
    url(r'^permissao/add/(?P<id>\d+)/$', CadastraPermissaoView.as_view(), name='cadastra_permissao'),
    url(r'^permissao/edit/(?P<id>\d+)/(?P<id_aluno>\d+)/$', EditaPermissaoView.as_view(), name='edita_permissao'),
    url(r'^tipo_permissao/add/$', CadastraTipoPermissaoView.as_view(), name='cadastra_tipo_permissao'),
    url(r'^tipo_oferta/add/$', CadastraTipoOfertaView.as_view(), name='cadastra_tipo_oferta'),
    url(r'^permissao/lista/$', PermissoesListaView.as_view(), name='lista_permissao'),
    url(r'^aluno/add/$', CadastroAlunoView.as_view(), name='cadastra_aluno'),
    url(r'^aluno/edit/(?P<id>\d+)/$', EdicaoAlunoView.as_view(), name='edita_aluno'),
    url(r'^funcionario/add/$', CadastraFuncionarioView.as_view(), name='cadastra_funcionario'),
    url(r'^funcionario/edit/(?P<id>\d+)/$', EditaFuncionarioView.as_view(), name='edita_funcionario'),
    url(r'^permissao/valida/professor/(?P<id>\d+)/$', ValidaPermissaoProfessorView.as_view(), name='valida_permissao_professor'),
    url(r'^permissao/valida/portaria/(?P<id>\d+)/$', ValidaPermissaoPortariaView.as_view(), name='valida_permissao_portaria'),
    url(r'^turma/add/$', CadastraTurmaView.as_view(), name='cadastra_turma'),
    url(r'^turma/edit/(?P<id>\d+)/$', EditaTurmaView.as_view(), name='edita_turma'),
    url(r'^curso/add/$', CadastraCursoView.as_view(), name='cadastra_curso'),
    url(r'^curso/edit/(?P<id>\d+)/$', EditaCursoView.as_view(), name='edita_curso'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
    url(r'^gera_comprovante/(?P<id>\d+)/$', views.GeraComprovantePDF, name='gera_comprovante'),
    url(r'^aluno/list/$', AlunoList.as_view(), name='aluno_list'),
    url(r'^funcionario/list/$', FuncionarioList.as_view(), name='funcionario_list'),
    url(r'^turma/list/$', TurmaList.as_view(), name='turma_list'),
    url(r'^curso/list/$', CursoList.as_view(), name='curso_list'),
    url(r'^remove/aluno/(?P<id>\d+)/$', views.exclui_aluno, name='exclui_aluno'),
    url(r'^seleciona/aluno/$', ListaAlunoView.as_view(), name='seleciona_aluno'),
    url(r'^remove/funcionario/(?P<id>\d+)/$', views.exclui_funcionario, name='exclui_funcionario'),
    url(r'^remove/permissao/(?P<id>\d+)/$', views.exclui_permissao, name='exclui_permissao'),
    url(r'^remove/turma/(?P<id>\d+)/$', views.exclui_turma, name='exclui_turma'),
    url(r'^remove/curso/(?P<id>\d+)/$', views.exclui_curso, name='exclui_curso'),
]

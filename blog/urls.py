from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login_verifica_grupo),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^permissao/add/$', views.cadastra_permissao, name='cadastra_permissao'),
    url(r'^permissao/lista/$', views.lista_permissoes, name='lista_permissao'),
    url(r'^aluno/add/$', views.cadastra_aluno, name='cadastra_aluno'),
    url(r'^funcionario/add/$', views.cadastra_funcionario, name='cadastra_funcionario'),
    url(r'^permissao/valida/professor/(?P<id>\d+)/$', views.ValidaPermissaoProfessor, name='valida_permissao_professor'),
    url(r'^permissao/valida/portaria/(?P<id>\d+)/$', views.ValidaPermissaoPortaria, name='valida_permissao_professor'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    # url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    # url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
    url(r'^gera_comprovante/(?P<id>\d+)/$', views.GeraComprovantePDF, name='gera_comprovante'),
    # #url(r'', include('blog.urls')),
    # url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	# url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]

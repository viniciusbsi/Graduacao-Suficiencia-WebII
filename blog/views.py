# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from blog.models import Permissao
from blog.forms import *
from django.shortcuts import render, get_object_or_404
from blog.forms import *
from django.shortcuts import redirect
from datetime import date
from django.contrib.auth.models import Group, User


# Pra gerar PDF e Zip#
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def login_verifica_grupo(request):
    if request.user.groups.all():
        if request.user.groups.get().name == "Nupe":
            return render(request, 'blog/funcionario_nupe.html')

        if request.user.groups.get().name == "Aluno":
            return render(request, 'blog/aluno.html')

        if request.user.groups.get().name == "Portaria":
            return render(request, 'blog/funcionario_portaria.html')

        if request.user.groups.get().name == "Professor":
            return render(request, 'blog/professor.html')

    return render(request, 'registration/login.html')


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})
#
@login_required
def cadastra_permissao(request):
    if request.method == "POST":
        form = PermissaoForm(request.POST)
        if form.is_valid():
            permissao = form.save(commit=False)
            funcionario = Funcionario.objects.get(pessoa_funcionario=request.user.id)
            permissao.funcionario_nupe = funcionario
            permissao.data = date.today()
            permissao.save()
            return redirect('blog.views.login_verifica_grupo')
    else:
        form = PermissaoForm()
    return render(request, 'blog/permissaoAdd.html', {'form': form})


def lista_permissoes(request):
    permissoes = Permissao.objects.all().order_by('data')
    return render(request, 'blog/permissaoLista.html', {'permissoes': permissoes})


@login_required
def cadatra_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        form_pessoa = PessoaForm(request.POST)
        form_senha = PessoaPasswordForm(request.POST)
        if form.is_valid() and form_pessoa.is_valid():
            form_pessoa.save()
            user = User.objects.last()
            grupo = Group.objects.get(name="Nupe")
            user.groups.add(grupo)
            user.set_password(request.POST['password'])
            user.save()

            obj = form.save(commit=False)
            obj.pessoa_aluno = User.objects.last()
            obj.save()
            return redirect('blog.views.login_verifica_grupo')
    else:
        form = AlunoForm()
        form_pessoa = PessoaForm()
        form_senha = PessoaPasswordForm()
    return render(request, 'blog/alunoAdd.html', {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha})


@login_required
def cadatra_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        form_pessoa = PessoaForm(request.POST)
        form_senha = PessoaPasswordForm(request.POST)
        if form.is_valid() and form_pessoa.is_valid():
            form_pessoa.save()
            user = User.objects.last()
            user.set_password(request.POST['password'])
            user.save()
            obj = form.save(commit=False)
            obj.pessoa_funcionario = User.objects.last()
            obj.save()
            return redirect('blog.views.login_verifica_grupo')
        else:
            print(form_pessoa.errors)
            print(form.errors)
    else:
        form = FuncionarioForm()
        form_pessoa = PessoaForm()
        form_senha = PessoaPasswordForm()
    return render(request, 'blog/funcionarioAdd.html', {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha})


# @login_required
# def cadatra_funcionario_portaria(request):
#     if request.method == "POST":
#         form = FuncionarioForm(request.POST)
#         form_pessoa = PessoaForm(request.POST)
#         form_senha = PessoaPasswordForm(request.POST)
#         if form.is_valid() and form_pessoa.is_valid() and form_senha.is_valid():
#             form_pessoa.save()
#             user = User.objects.last()
#             grupo = Group.objects.get(name="Portaria")
#             user.groups.add(grupo)
#             user.set_password(request.POST['password'])
#             user.save()
#
#             obj = form.save(commit=False)
#             obj.pessoa_funcionario = User.objects.last()
#             obj.save()
#             return redirect('blog.views.login_verifica_grupo')
#     else:
#         form = FuncionarioForm()
#         form_pessoa = PessoaForm()
#         form_senha = PessoaPasswordForm()
#     return render(request, 'blog/funcionarioPortariaAdd.html', {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha})
#
# @login_required
# def cadatra_professor(request):
#     if request.method == "POST":
#         form = FuncionarioForm(request.POST)
#         form_pessoa = PessoaForm(request.POST)
#         form_senha = PessoaPasswordForm(request.POST)
#         if form.is_valid() and form_pessoa.is_valid():
#             form_pessoa.save()
#             user = User.objects.last()
#             grupo = Group.objects.get(name="Professor")
#             user.groups.add(grupo)
#             user.set_password(request.POST['password'])
#             user.save()
#
#             obj = form.save(commit=False)
#             obj.pessoa_funcionario = User.objects.last()
#             obj.save()
#             return redirect('blog.views.login_verifica_grupo')
#     else:
#         form = FuncionarioForm()
#         form_pessoa = PessoaForm()
#         form_senha = PessoaPasswordForm()
#     return render(request, 'blog/funcionarioProfessorAdd.html', {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha})


@login_required
def GeraComprovantePDF(request, id=None):

    permissao = Permissao.objects.get(pk=id)
    nome = "static/media/comprovantes/" + str(permissao.aluno.pessoa_aluno.get_full_name()) + ".pdf"
    doc = SimpleDocTemplate("blog/static/media/comprovantes/" + str(permissao.aluno.pessoa_aluno.get_full_name()) + ".pdf", pagesize=letter, rightMargin=72,
                            leftMargin=72, topMargin=00, bottomMargin=18)

    Story = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, spaceBefore=20))
    styles.add(ParagraphStyle(name='inicial', alignment=TA_JUSTIFY, spaceBefore=50))
    styles.add(ParagraphStyle(name='linhas', alignment=TA_JUSTIFY, spaceBefore=20))

    Story.append(Paragraph(u"Eu <b>%s</b> na qualidade de <b>%s</b> do Núcleo pedagógico, apresento justificativa "
                           u"para o discente <b>%s</b> para entrada/saída sob justificativa de <b>%s</b> na data de "
                           u"<b>%s</b> às <b>%s</b>. Declaro que a portaria encontra-se sob responsabilidade de <b>%s</b>" %
                           (permissao.funcionario_nupe.pessoa_funcionario.get_full_name(),
                            permissao.funcionario_nupe.funcao, permissao.aluno.pessoa_aluno.get_full_name(),
                            permissao.descricao, str(permissao.data), permissao.hora_solicitada,
                            permissao.funcionario_portaria.pessoa_funcionario.get_full_name()), styles["inicial"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)
    return redirect("/" + nome)

# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'blog/post_edit.html', {'form': form})
#
# @login_required
# def post_draft_list(request):
#     posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
#     return render(request, 'blog/post_draft_list.html', {'posts': posts})
#
# @login_required
# def post_publish(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.publish()
#     return redirect('blog.views.post_detail', pk=pk)
#
# def publish(self):
#     self.published_date = timezone.now()
#     self.save()
#
# @login_required
# def post_remove(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post.delete()
#     return redirect('blog.views.post_list')
#
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})
#
# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('blog.views.post_detail', pk=comment.post.pk)
#
# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post_pk = comment.post.pk
#     comment.delete()
#     return redirect('blog.views.post_detail', pk=post_pk)

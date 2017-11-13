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
            return render(request, 'blog/funcionario_nupe.html', {'grupo_user': 'nupe'})

        if request.user.groups.get().name == "Portaria":
            permissoes = Permissao.objects.all().order_by('data')
            return render(request, 'blog/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'portaria'})

        if request.user.groups.get().name == "Professor":
            permissoes = Permissao.objects.all().order_by('data')
            return render(request, 'blog/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'professor'})

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
            print (request.user.id)
            funcionario = Funcionario.objects.get(pessoa_funcionario=request.user.id)
            permissao.funcionario_nupe = funcionario
            permissao.data = date.today()
            permissao.save()
            msg = "Permissão cadastrada com sucesso!"
            return render(request, 'blog/funcionario_nupe.html', {'msg': msg})
        else:
            print form.errors
    else:
        form = PermissaoForm()
    return render(request, 'blog/permissaoAdd.html', {'form': form})


@login_required
def cadastra_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Curso cadastrado com sucesso!"
            return render(request, 'blog/funcionario_nupe.html', {'msg': msg})
        else:
            print form.errors
    else:
        form = CursoForm()
    return render(request, 'blog/cursoAdd.html', {'form': form})


@login_required
def cadastra_turma(request):
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Turma cadastrada com sucesso!"
            return render(request, 'blog/funcionario_nupe.html', {'msg': msg})
        else:
            print form.errors
    else:
        form = TurmaForm()
    return render(request, 'blog/turmaAdd.html', {'form': form})


def lista_permissoes(request):
    permissoes = Permissao.objects.all().order_by('data')
    return render(request, 'blog/permissaoLista.html', {'permissoes': permissoes})


@login_required
def cadastra_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Aluno cadastrado com sucesso!"
            return render(request, 'blog/funcionario_nupe.html', {'msg': msg})

        else:
            print (form.errors)
    else:
        form = AlunoForm()
    return render(request, 'blog/alunoAdd.html', {'form': form})


@login_required
def cadastra_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        form_pessoa = PessoaForm(request.POST)
        form_senha = PessoaPasswordForm(request.POST)
        if form.is_valid() and form_pessoa.is_valid() and form_senha.is_valid():
            form_pessoa.save()
            user = User.objects.last()
            user.set_password(request.POST['password'])
            grupo = Group.objects.get(pk=request.POST['groups'])
            user.groups.add(grupo)
            user.save()
            obj = form.save(commit=False)
            obj.pessoa_funcionario = User.objects.last()
            obj.save()
            msg = "Funcionário cadastrado com sucesso!"
            return render(request, 'blog/funcionario_nupe.html', {'msg': msg})
        else:
            print(form_pessoa.errors)
            print(form_pessoa.errors)
            print(form.errors)
    else:
        form = FuncionarioForm()
        form_pessoa = PessoaForm()
        form_senha = PessoaPasswordForm()
    return render(request, 'blog/funcionarioAdd.html', {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha})


@login_required
def GeraComprovantePDF(request, id=None):

    permissao = Permissao.objects.get(pk=id)
    nome = "static/media/comprovantes/" + str(permissao.aluno.nome) + ".pdf"
    doc = SimpleDocTemplate("blog/static/media/comprovantes/" + str(permissao.aluno.nome) + ".pdf", pagesize=letter, rightMargin=72,
                            leftMargin=72, topMargin=00, bottomMargin=18)

    Story = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, spaceBefore=20))
    styles.add(ParagraphStyle(name='inicial', alignment=TA_JUSTIFY, spaceBefore=50))
    styles.add(ParagraphStyle(name='linhas', alignment=TA_JUSTIFY, spaceBefore=20))

    Story.append(Paragraph(u"Eu <b>%s</b> na qualidade de servidor do Núcleo pedagógico, apresento justificativa "
                           u"para o discente <b>%s</b> para entrada/saída sob justificativa de <b>%s</b> na data de "
                           u"<b>%s</b> às <b>%s</b>" % (permissao.funcionario_nupe.pessoa_funcionario.get_full_name(),permissao.aluno.nome,
                            permissao.descricao, str(permissao.data), permissao.hora_solicitada), styles["inicial"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)
    return redirect("/" + nome)


@login_required
def ValidaPermissaoProfessor(request, id=None):
    permissao = Permissao.objects.get(pk=id)
    permissao.verificado_professor = Funcionario.objects.get(pessoa_funcionario=request.user.id)
    permissao.save()
    permissoes = Permissao.objects.all()
    return render(request, 'blog/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'professor'})


@login_required
def ValidaPermissaoPortaria(request, id=None):
    permissao = Permissao.objects.get(pk=id)
    permissao.verificado_portaria = Funcionario.objects.get(pessoa_funcionario=request.user.id)
    permissao.save()
    permissoes = Permissao.objects.all()
    return render(request, 'blog/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'portaria'})

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

# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from web1.forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import Group, User
from django.db.models import Q
from django.views.generic.edit import UpdateView


# Pra gerar PDF#
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import date


class AlunoList(ListView):
    queryset = Aluno.objects.all().exclude(excluido=True)
    template_name = 'web1/alunosLista.html'

class FuncionarioList(ListView):
    context_object_name = 'object_list'
    queryset = Funcionario.objects.all().exclude(excluido=True)
    template_name = 'web1/funcionariosLista.html'

class CursoList(ListView):
    queryset = Curso.objects.all().exclude(excluido=True)
    template_name = 'web1/cursosLista.html'

class TurmaList(ListView):
    queryset = Turma.objects.all().exclude(excluido=True)
    template_name = 'web1/turmasLista.html'


def login_verifica_grupo(request):
    if request.user.is_authenticated():
        if request.user.groups.all():
            if request.user.groups.get().name == "Nupe":
                return render(request, 'web1/funcionario_nupe.html', {'grupo_user': 'nupe'})

            if request.user.groups.get().name == "Portaria":
                permissoes = Permissao.objects.all().order_by('data')
                return render(request, 'web1/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'portaria'})

            if request.user.groups.get().name == "Professor":
                permissoes = Permissao.objects.all().order_by('data')
                return render(request, 'web1/permissaoLista.html',
                              {'permissoes': permissoes, 'grupo_user': 'professor'})
    else:
        return redirect('/accounts/login/')


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
            msg = "Permissão cadastrada com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = PermissaoForm()
    return render(request, 'web1/permissaoAdd.html', {'form': form, 'grupo_user': 'nupe'})


@login_required
def edita_permissao(request, id):
    permissao = Permissao.objects.get(pk=id)
    if request.method == "POST":
        form = PermissaoForm(request.POST, instance=permissao)
        if form.is_valid():
            permissao = form.save(commit=False)
            funcionario = Funcionario.objects.get(pessoa_funcionario=request.user.id)
            permissao.funcionario_nupe = funcionario
            permissao.data = date.today()
            permissao.save()
            msg = "Permissão editada com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = PermissaoForm(instance=permissao)
    return render(request, 'web1/permissaoAdd.html', {'form': form, 'grupo_user': 'nupe', 'permissao': permissao})


@login_required
def cadastra_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Curso cadastrado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = CursoForm()
    return render(request, 'web1/cursoAdd.html', {'form': form, 'grupo_user': 'nupe'})


@login_required
def edita_curso(request, id):
    curso = Curso.objects.get(pk=id)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            msg = "Curso editado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = CursoForm(instance=curso)
    return render(request, 'web1/cursoAdd.html', {'form': form, 'grupo_user': 'nupe', 'curso': curso})


@login_required
def cadastra_turma(request):
    if request.method == "POST":
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Turma cadastrada com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = TurmaForm()
    return render(request, 'web1/turmaAdd.html', {'form': form, 'grupo_user': 'nupe'})

@login_required
def edita_turma(request, id):
    turma = Turma.objects.get(pk=id)
    if request.method == "POST":
        form = TurmaForm(request.POST, instance=turma)
        if form.is_valid():
            form.save()
            msg = "Turma editada com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = TurmaForm(instance=turma)
    return render(request, 'web1/turmaAdd.html', {'form': form, 'grupo_user': 'nupe', 'turma': turma})


@login_required
def cadastra_tipo_permissao(request):
    if request.method == "POST":
        form = TipoPermissaoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Tipo de permissão cadastrada com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = TipoPermissaoForm()
    return render(request, 'web1/tipoPermissaoAdd.html', {'form': form, 'grupo_user': 'nupe'})

@login_required
def cadastra_tipo_oferta(request):
    if request.method == "POST":
        form = TipoOfertaForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Tipo de oferta cadastrada com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print form.errors
    else:
        form = TipoOfertaForm()
    return render(request, 'web1/tipoOfertaAdd.html', {'form': form, 'grupo_user': 'nupe'})


def lista_permissoes(request):
    if 'filtro' in request.GET:
        permissoes = Permissao.objects.filter(Q(aluno__nome__icontains=request.GET.get('filtro'))|
            Q(aluno__curso__descricao__icontains=request.GET.get('filtro'))|
            Q(aluno__turma__descricao__icontains=request.GET.get('filtro'))).exclude(excluido=True)
    else:
        permissoes = Permissao.objects.all().order_by('data').exclude(excluido=True)
    return render(request, 'web1/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'nupe'})


@login_required
def cadastra_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Aluno cadastrado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})

        else:
            print (form.errors)
    else:
        form = AlunoForm()
    return render(request, 'web1/alunoAdd.html', {'form': form, 'grupo_user': 'nupe'})

@login_required
def edita_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            msg = "Aluno editado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})

        else:
            print (form.errors)
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'web1/alunoAdd.html', {'form': form, 'grupo_user': 'nupe', 'aluno': aluno})

@login_required
def edita_funcionario(request, id):
    funcionario = Funcionario.objects.get(pk=id)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        form_pessoa = PessoaForm(request.POST, instance=funcionario.pessoa_funcionario)
        form_senha = PessoaPasswordForm(request.POST)
        if form.is_valid() and form_pessoa.is_valid() and form_senha.is_valid():
            obj_pessoa = form_pessoa.save(commit=False)
            grupo = Group.objects.get(pk=request.POST['groups'])
            obj_pessoa.save()
            obj_pessoa.groups.add(grupo)
            user = User.objects.last()
            user.set_password(request.POST['password'])
            user.save()
            obj = form.save(commit=False)
            obj.pessoa_funcionario = User.objects.last()
            obj.save()
            msg = "Funcionário editado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print(form_pessoa.errors)
            print(form_senha.errors)
            print(form.errors)
    else:
        form = FuncionarioForm(instance=funcionario)
        form_pessoa = PessoaForm(instance=funcionario.pessoa_funcionario)
        form_senha = PessoaPasswordForm()
    return render(request, 'web1/funcionarioAdd.html',
                  {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha, 'grupo_user': 'nupe', 'funcionario': funcionario})

@login_required
def cadastra_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        form_pessoa = PessoaForm(request.POST)
        form_senha = PessoaPasswordForm(request.POST)
        if form.is_valid() and form_pessoa.is_valid() and form_senha.is_valid():
            obj_pessoa = form_pessoa.save(commit=False)
            grupo = Group.objects.get(pk=request.POST['groups'])
            obj_pessoa.save()
            obj_pessoa.groups.add(grupo)
            user = User.objects.last()
            user.set_password(request.POST['password'])
            user.save()
            obj = form.save(commit=False)
            obj.pessoa_funcionario = User.objects.last()
            obj.save()
            msg = "Funcionário cadastrado com sucesso!"
            return render(request, 'web1/funcionario_nupe.html', {'msg': msg, 'grupo_user': 'nupe'})
        else:
            print(form_pessoa.errors)
            print(form_senha.errors)
            print(form.errors)
    else:
        form = FuncionarioForm()
        form_pessoa = PessoaForm()
        form_senha = PessoaPasswordForm()
    return render(request, 'web1/funcionarioAdd.html',
                  {'form': form, 'form_pessoa': form_pessoa, 'form_senha': form_senha, 'grupo_user': 'nupe'})

@login_required
def GeraComprovantePDF(request, id=None):
    permissao = Permissao.objects.get(pk=id)
    nome = "static/comprovantes/" + str(permissao.aluno.nome) + ".pdf"
    doc = SimpleDocTemplate("static/comprovantes/" + str(permissao.aluno.nome) + ".pdf", pagesize=letter,
                            rightMargin=72,
                            leftMargin=72, topMargin=00, bottomMargin=18)

    Story = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY, spaceBefore=20))
    styles.add(ParagraphStyle(name='inicial', alignment=TA_CENTER, spaceBefore=30, spaceAfter=50, fontSize=15))
    styles.add(ParagraphStyle(name='linhas', alignment=TA_JUSTIFY, spaceBefore=20))

    Story.append(Paragraph(u"<b>Autorização</b>", styles["inicial"]))
    Story.append(Paragraph(u"Eu <b>%s</b> na qualidade de servidor do Núcleo pedagógico, apresento justificativa "
                           u"para o discente <b>%s</b> para <b>%s</b> sob justificativa de <b>%s</b> na data de "
                           u"<b>%s</b> às <b>%s</b>" % (
                               permissao.funcionario_nupe.pessoa_funcionario.get_full_name(), permissao.aluno.nome,
                               permissao.tipo_permissao.descricao,
                               permissao.descricao, str(permissao.data.strftime('%d/%m/%Y')),
                               str(permissao.hora_solicitada)[:-3] + "h"), styles["linhas"]))
    Story.append(Spacer(1, 12))
    doc.build(Story)
    return redirect("/" + nome)


@login_required
def ValidaPermissaoProfessor(request, id=None):
    permissao = Permissao.objects.get(pk=id)
    permissao.verificado_professor = Funcionario.objects.get(pessoa_funcionario=request.user.id)
    permissao.save()
    permissoes = Permissao.objects.all()
    return render(request, 'web1/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'professor'})


@login_required
def ValidaPermissaoPortaria(request, id=None):
    permissao = Permissao.objects.get(pk=id)
    permissao.verificado_portaria = Funcionario.objects.get(pessoa_funcionario=request.user.id)
    permissao.save()
    permissoes = Permissao.objects.all()
    return render(request, 'web1/permissaoLista.html', {'permissoes': permissoes, 'grupo_user': 'portaria'})


@login_required
def exclui_aluno(request, id):
    obj = Aluno.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Aluno removido com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_funcionario(request, id):
    obj = Funcionario.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Funcionário removido com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_permissao(request, id):
    obj = Permissao.objects.get(pk=id)
    obj.excluido     = True
    obj.save()
    msg = "Permissao removida com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_curso(request, id):
    obj = Curso.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Curso removido com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

@login_required
def exclui_turma(request, id):
    obj = Turma.objects.get(pk=id)
    obj.excluido = True
    obj.save()
    msg = "Turma removida com sucesso!"
    return render(request, 'web1/funcionario_nupe.html', {'msg': msg})

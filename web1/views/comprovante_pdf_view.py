# coding: utf-8
from django.contrib.auth.decorators import login_required
from web1.models.permissao_model import Permissao
from django.shortcuts import redirect

# Pra gerar PDF#
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


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
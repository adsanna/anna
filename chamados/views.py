from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from .models import Documentos, STATUS_CHOICE


def home(request):
    # HOME (pode listar tudo, como você já fazia)
    documentos = Documentos.objects.all()

    q = request.GET.get('q')
    if q:
        documentos = documentos.filter(titulo__icontains=q)

    data = request.GET.get('data')
    if data == 'recentes':
        documentos = documentos.order_by('-data_de_criacao')
    elif data == 'antigos':
        documentos = documentos.order_by('data_de_criacao')
    else:
        documentos = documentos.order_by('-data_de_criacao')

    status = request.GET.get('status')
    if status:
        documentos = documentos.filter(status=status)

    return render(request, 'usuarios/home.html', {
        'documentos': documentos
    })


def novo_chamado(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        departamento = request.POST.get('departamento')
        arquivo = request.FILES.get('arquivo')

        if titulo:
            doc = Documentos(
                titulo=titulo,
                descricao=descricao,
                departamento=departamento,
                usuario=request.user if request.user.is_authenticated else None,
                arquivo=arquivo
            )
            doc.save()
            return redirect('meus_chamados')  # ✅ melhor UX: volta pro histórico do usuário

    return render(request, 'usuarios/novo_chamado.html')


@login_required
def meus_chamados(request):
    documentos = Documentos.objects.filter(usuario=request.user).order_by('-data_de_criacao')
    return render(request, 'usuarios/home.html', {'documentos': documentos})


# ==========================
# ADMIN (SÓ STAFF)
# ==========================
@staff_member_required
def admin_chamados(request):
    documentos = Documentos.objects.all()

    q = request.GET.get('q')
    if q:
        documentos = documentos.filter(
            Q(titulo__icontains=q) |
            Q(descricao__icontains=q) |
            Q(departamento__icontains=q) |
            Q(usuario__username__icontains=q)
        )

    data = request.GET.get('data')
    if data == 'recentes':
        documentos = documentos.order_by('-data_de_criacao')
    elif data == 'antigos':
        documentos = documentos.order_by('data_de_criacao')
    else:
        documentos = documentos.order_by('-data_de_criacao')

    status = request.GET.get('status')
    if status:
        documentos = documentos.filter(status=status)

    return render(request, 'usuarios/admin.html', {
        'documentos': documentos,
        'status_choices': STATUS_CHOICE
    })


@staff_member_required
def admin_detalhe_chamado(request, pk):
    doc = get_object_or_404(Documentos, pk=pk)

    if request.method == "POST":
        # se marcou, vira concluído; se desmarcou, volta pra "em andamento" (ou "aberto", você escolhe)
        marcado = request.POST.get("marcar_concluido")

        if marcado:
            doc.status = "concluído"
        else:
            doc.status = "em andamento"  # você pode trocar pra "aberto" se preferir

        doc.save()
        return redirect('admin_detalhe_chamado', pk=doc.pk)

    return render(request, 'usuarios/admin_detalhe.html', {"doc": doc})

    
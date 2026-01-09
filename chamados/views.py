from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Documentos

def home(request):
    documentos = Documentos.objects.all()

    q = request.GET.get('q')
    if q:
        documentos = documentos.filter(titulo__icontains=q)

    data = request.GET.get('data')
    if data == 'recentes':
        documentos = documentos.order_by('-data_de_criacao')
    elif data == 'antigos':
        documentos = documentos.order_by('data_de_criacao')

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
            return redirect('home')

    return render(request, 'usuarios/novo_chamado.html')

def meus_chamados(request):
    documentos = Documentos.objects.filter(usuario=request.user).order_by('-data_de_criacao')
    return render(request, 'usuarios/home.html', {'documentos': documentos})

def documentos(request):
    documentos_lista = {
        'documentos': Documentos.objects.all().order_by('-data_de_criacao')
    }
    return render(request, 'usuarios/home.html', documentos_lista)
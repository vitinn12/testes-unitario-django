from django.shortcuts import render, redirect
from django.contrib import messages as message
from django.http import HttpResponse
from .models import Usuario

# Create your views here.

def index(request):
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})

def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        if nome and idade:
            Usuario.objects.create(nome=nome, idade=idade)
            message.success(request, 'Dados salvo no banco')
            return redirect('index')
        else:
            message.error(request, 'Erro de digitação')
            return render(request, 'index.html')

    return render(request, 'index.html')


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios}) 

def excluir_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    message.success(request, 'Usuário excluído')
    return redirect('index')
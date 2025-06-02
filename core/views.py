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
            # Salva o usuário no banco de dados
            Usuario.objects.create(nome=nome, idade=idade)
            message.success(request, 'Nome e idade salvos com sucesso!')
            return redirect('index')
        else:
            message.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'index.html')

    return render(request, 'index.html')


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios}) 

def editar_usuario(request, id):
    usuario_obj = Usuario.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        if nome and idade:
            usuario_obj.nome = nome
            usuario_obj.idade = idade
            usuario_obj.save()
            message.success(request, 'Usuário atualizado com sucesso!')
            return render(request, 'listar_usuarios.html', {'usuarios': Usuario.objects.all()})
        else:
            message.error(request, 'Por favor, preencha todos os campos.')
    
    return render(request, 'editar_usuario.html', {'usuario': usuario_obj})

def excluir_usuario(request, id):
    usuario_obj = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario_obj.delete()
        message.success(request, 'Usuário excluído com sucesso!')
        return render(request, 'listar_usuarios.html', {'usuarios': Usuario.objects.all()})
    
    return render(request, 'excluir_usuario.html', {'usuario': usuario_obj})
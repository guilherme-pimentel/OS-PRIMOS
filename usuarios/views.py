from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista.html', {'usuarios': usuarios})

def adicionar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        Usuario.objects.create(nome=nome, email=email, endereco=endereco)
        return redirect('lista_usuarios')
    return render(request, 'usuarios/adicionar.html')

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.email = request.POST.get('email')
        usuario.endereco = request.POST.get('endereco')
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'usuarios/editar.html', {'usuario': usuario})

def excluir_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    usuario.delete()
    return redirect('lista_usuarios')

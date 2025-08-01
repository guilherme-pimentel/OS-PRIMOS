from django.shortcuts import render, redirect, get_object_or_404
from .models import Medidor
from usuarios.models import Usuario

def lista_medidores(request):
    medidores = Medidor.objects.all()
    return render(request, 'medidores/lista.html', {'medidores': medidores})

def adicionar_medidor(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        numero_serie = request.POST.get('numero_serie')
        localizacao = request.POST.get('localizacao')
        data_instalacao = request.POST.get('data_instalacao')
        usuario_id = request.POST.get('usuario')
        usuario = Usuario.objects.get(id=usuario_id)
        Medidor.objects.create(
            numero_serie=numero_serie,
            localizacao=localizacao,
            data_instalacao=data_instalacao,
            usuario=usuario
        )
        return redirect('lista_medidores')
    return render(request, 'medidores/adicionar.html', {'usuarios': usuarios})

def editar_medidor(request, id):
    medidor = get_object_or_404(Medidor, id=id)
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        medidor.numero_serie = request.POST.get('numero_serie')
        medidor.localizacao = request.POST.get('localizacao')
        medidor.data_instalacao = request.POST.get('data_instalacao')
        usuario_id = request.POST.get('usuario')
        medidor.usuario = Usuario.objects.get(id=usuario_id)
        medidor.save()
        return redirect('lista_medidores')
    return render(request, 'medidores/editar.html', {'medidor': medidor, 'usuarios': usuarios})

def excluir_medidor(request, id):
    medidor = get_object_or_404(Medidor, id=id)
    medidor.delete()
    return redirect('lista_medidores')

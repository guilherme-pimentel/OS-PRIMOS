from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento
from usuarios.models import Usuario

def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/lista.html', {'equipamentos': equipamentos})

def adicionar_equipamento(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        potencia = request.POST.get('potencia_watts')
        horas = request.POST.get('horas_uso_diario')
        usuario_id = request.POST.get('usuario')
        usuario = Usuario.objects.get(id=usuario_id)
        Equipamento.objects.create(
            nome=nome,
            potencia_watts=potencia,
            horas_uso_diario=horas,
            usuario=usuario
        )
        return redirect('lista_equipamentos')
    return render(request, 'equipamentos/adicionar.html', {'usuarios': usuarios})

def editar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        equipamento.nome = request.POST.get('nome')
        equipamento.potencia_watts = request.POST.get('potencia_watts')
        equipamento.horas_uso_diario = request.POST.get('horas_uso_diario')
        equipamento.usuario = Usuario.objects.get(id=request.POST.get('usuario'))
        equipamento.save()
        return redirect('lista_equipamentos')
    return render(request, 'equipamentos/editar.html', {'equipamento': equipamento, 'usuarios': usuarios})

def excluir_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.delete()
    return redirect('lista_equipamentos')

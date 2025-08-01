from django.shortcuts import render, redirect, get_object_or_404
from .models import Leitura
from medidores.models import Medidor

def lista_leituras(request):
    leituras = Leitura.objects.all()
    return render(request, 'leituras/lista.html', {'leituras': leituras})

def adicionar_leitura(request):
    medidores = Medidor.objects.all()
    if request.method == 'POST':
        data = request.POST.get('data')
        consumo = request.POST.get('consumo_kwh')
        medidor_id = request.POST.get('medidor')
        medidor = Medidor.objects.get(id=medidor_id)
        Leitura.objects.create(data=data, consumo_kwh=consumo, medidor=medidor)
        return redirect('lista_leituras')
    return render(request, 'leituras/adicionar.html', {'medidores': medidores})

def editar_leitura(request, id):
    leitura = get_object_or_404(Leitura, id=id)
    medidores = Medidor.objects.all()
    if request.method == 'POST':
        leitura.data = request.POST.get('data')
        leitura.consumo_kwh = request.POST.get('consumo_kwh')
        leitura.medidor = Medidor.objects.get(id=request.POST.get('medidor'))
        leitura.save()
        return redirect('lista_leituras')
    return render(request, 'leituras/editar.html', {'leitura': leitura, 'medidores': medidores})

def excluir_leitura(request, id):
    leitura = get_object_or_404(Leitura, id=id)
    leitura.delete()
    return redirect('lista_leituras')

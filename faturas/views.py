from django.shortcuts import render, redirect, get_object_or_404
from .models import Fatura
from leituras.models import Leitura

def lista_faturas(request):
    faturas = Fatura.objects.all()
    return render(request, 'faturas/lista.html', {'faturas': faturas})

def adicionar_fatura(request):
    leituras = Leitura.objects.all()
    if request.method == 'POST':
        data_emissao = request.POST.get('data_emissao')
        valor = request.POST.get('valor')
        leitura_id = request.POST.get('leitura')
        paga = 'paga' in request.POST
        leitura = Leitura.objects.get(id=leitura_id)
        Fatura.objects.create(data_emissao=data_emissao, valor=valor, leitura=leitura, paga=paga)
        return redirect('lista_faturas')
    return render(request, 'faturas/adicionar.html', {'leituras': leituras})

def editar_fatura(request, id):
    fatura = get_object_or_404(Fatura, id=id)
    leituras = Leitura.objects.all()
    if request.method == 'POST':
        fatura.data_emissao = request.POST.get('data_emissao')
        fatura.valor = request.POST.get('valor')
        fatura.paga = 'paga' in request.POST
        leitura_id = request.POST.get('leitura')
        fatura.leitura = Leitura.objects.get(id=leitura_id)
        fatura.save()
        return redirect('lista_faturas')
    return render(request, 'faturas/editar.html', {'fatura': fatura, 'leituras': leituras})

def excluir_fatura(request, id):
    fatura = get_object_or_404(Fatura, id=id)
    fatura.delete()
    return redirect('lista_faturas')

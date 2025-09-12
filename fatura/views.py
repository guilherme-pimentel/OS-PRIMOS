from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Fatura
from .forms import FaturaForm


@login_required
@permission_required('faturas.view_fatura', raise_exception=True)
def lista_faturas(request):
    faturas = Fatura.objects.all()
    return render(request, 'fatura/lista.html', {'faturas': faturas})


@login_required
@permission_required('faturas.view_fatura', raise_exception=True)
def detalhe_fatura(request, id):
    fatura = get_object_or_404(Fatura, id=id)
    return render(request, 'fatura/detail.html', {'fatura': fatura})


@login_required
@permission_required('faturas.add_fatura', raise_exception=True)
def adicionar_fatura(request):
    if request.method == 'POST':
        form = FaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_fatura')
    else:
        form = FaturaForm()
    return render(request, 'fatura/adicionar.html', {'form': form})


@login_required
@permission_required('faturas.change_fatura', raise_exception=True)
def editar_fatura(request, id):
    fatura = get_object_or_404(Fatura, id=id)
    if request.method == 'POST':
        form = FaturaForm(request.POST, instance=fatura)
        if form.is_valid():
            form.save()
            return redirect('lista_fatura')
    else:
        form = FaturaForm(instance=fatura)
    return render(request, 'fatura/editar.html', {'form': form, 'fatura': fatura})

@login_required
@permission_required('faturas.delete_fatura', raise_exception=True)
def excluir_fatura(request, id):
    fatura = get_object_or_404(Fatura, id=id)
    fatura.delete()
    return redirect('lista_fatura')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Avaliacao
from .forms import AvaliacaoForm
from matricula.models import Matricula
from funcionario.models import Funcionario


@login_required
def lista_avaliacao(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'avaliacao/lista.html', {'avaliacoes': avaliacoes})


@login_required
def adicionar_avaliacao(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_avaliacao')
    else:
        form = AvaliacaoForm()

    return render(request, 'avaliacao/adicionar.html', {'form': form})


@login_required
def editar_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('lista_avaliacao')
    else:
        form = AvaliacaoForm(instance=avaliacao)

    return render(request, 'avaliacao/editar.html', {'form': form, 'avaliacao': avaliacao})


@login_required
def detalhe_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    return render(request, 'avaliacao/detail.html', {'avaliacao': avaliacao})


@login_required
def excluir_avaliacao(request, id):
    avaliacao = get_object_or_404(Avaliacao, id=id)
    avaliacao.delete()
    return redirect('lista_avaliacao')

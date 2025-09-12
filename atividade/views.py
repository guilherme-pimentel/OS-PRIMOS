from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Atividade
from .forms import AtividadeForm


@login_required
@permission_required('atividade.view_atividade', raise_exception=True)
def lista_atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividade/lista.html', {'atividades': atividades})


@login_required
@permission_required('atividade.add_atividade', raise_exception=True)
def adicionar_atividade(request):
    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Atividade criada com sucesso!")
            return redirect('lista_atividades')
        else:
            messages.error(request, "Erro ao criar atividade. Verifique os dados.")
    else:
        form = AtividadeForm()

    return render(request, 'atividade/adicionar.html', {'form': form})


@login_required
@permission_required('atividade.change_atividade', raise_exception=True)
def editar_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)

    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            messages.success(request, "Atividade atualizada com sucesso!")
            return redirect('lista_atividades')
        else:
            messages.error(request, "Erro ao atualizar atividade.")
    else:
        form = AtividadeForm(instance=atividade)

    return render(request, 'atividade/editar.html', {'form': form, 'atividade': atividade})


@login_required
@permission_required('atividade.view_atividade', raise_exception=True)
def detalhe_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    return render(request, 'atividade/detail.html', {'atividade': atividade})


@login_required
@permission_required('atividade.delete_atividade', raise_exception=True)
def excluir_atividade(request, id):
    atividade = get_object_or_404(Atividade, id=id)
    try:
        atividade.delete()
        messages.success(request, "Atividade excluída com sucesso!")
    except Exception as e:
        messages.error(request, f"Erro ao excluir atividade: {str(e)}")
    return redirect('lista_atividades')

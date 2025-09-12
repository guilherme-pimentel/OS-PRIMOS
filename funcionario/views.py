from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario
from .forms import FuncionarioForm

@login_required
def lista_funcionario(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/lista.html', {'funcionarios': funcionarios})


@permission_required('funcionario.add_funcionario', raise_exception=True)
def adicionar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'funcionario/adicionar.html', {'form': form})


@permission_required('funcionario.change_funcionario', raise_exception=True)
def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        # não use funcionario.user, já que Funcionario herda User
        initial = {
            'username': funcionario.username,
            'email': funcionario.email,
        }
        form = FuncionarioForm(instance=funcionario, initial=initial)
    return render(request, 'funcionario/editar.html', {'form': form, 'funcionario': funcionario})


@permission_required('funcionario.delete_funcionario', raise_exception=True)
def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    funcionario.delete()  # já é um User, então basta deletar
    return redirect('lista_funcionarios')


@login_required
@permission_required('funcionario.view_funcionario', raise_exception=True)
def detalhe_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    return render(request, 'funcionario/detail.html', {'funcionario': funcionario})

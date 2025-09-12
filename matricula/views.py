from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Matricula
from .forms import MatriculaForm


@login_required
@permission_required('matricula.view_matricula', raise_exception=True)
def lista_matricula(request):
    matriculas = Matricula.objects.all()
    return render(request, 'matricula/lista.html', {'matriculas': matriculas})


@login_required
@permission_required('matricula.add_matricula', raise_exception=True)
def adicionar_matricula(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_matriculas')
    else:
        form = MatriculaForm()

    return render(request, 'matricula/adicionar.html', {'form': form})


@login_required
@permission_required('matricula.change_matricula', raise_exception=True)
def editar_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)

    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            return redirect('lista_matriculas')
    else:
        form = MatriculaForm(instance=matricula)

    return render(request, 'matricula/editar.html', {'form': form, 'matricula': matricula})


@login_required
@permission_required('matricula.view_matricula', raise_exception=True)
def detalhe_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    return render(request, 'matricula/detail.html', {'matricula': matricula})


@login_required
@permission_required('matricula.delete_matricula', raise_exception=True)
def excluir_matricula(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    matricula.delete()
    return redirect('lista_matriculas')

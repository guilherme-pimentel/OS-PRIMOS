from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from escola.models import Aluno, Professor, PerfilUsuario
from django.contrib.auth.decorators import login_required
from .forms import AlunoForm
from .forms import ProfessorForm

def home(request):
    return render(request, 'sistema_escolar/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login bem-sucedido
            login(request, user)
            messages.success(request, 'Login bem-sucedido!')

            try:
                perfil_usuario = PerfilUsuario.objects.get(user=user)  # Verificando o perfil do usuário
                perfil = perfil_usuario.perfil  # Atribuindo o perfil do usuário à variável "perfil"
                
                # Mensagem de depuração: Exibir o perfil do usuário no console
                print(f"Perfil do usuário: {perfil}")  # Isso vai ajudar a depurar

                # Redireciona de acordo com o perfil
                if perfil == 'ADMIN':
                    return redirect('admin_dashboard')
                elif perfil == 'PROF':
                    return redirect('professor_dashboard')
                elif perfil == 'ALUNO':
                    return redirect('aluno_dashboard')
                else:
                    messages.error(request, 'Perfil de usuário desconhecido.')
                    return render(request, 'sistema_escolar/home.html')
            except PerfilUsuario.DoesNotExist:
                messages.error(request, 'Perfil não encontrado.')
                return render(request, 'sistema_escolar/home.html')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'sistema_escolar/home.html')

def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'sistema_escolar/aluno_list.html', {'alunos': alunos})

def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm()
    return render(request, 'sistema_escolar/aluno_form.html', {'form': form})

def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'sistema_escolar/aluno_form.html', {'form': form})

def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    return render(request, 'sistema_escolar/aluno_confirm_delete.html', {'aluno': aluno})

def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'sistema_escolar/professor_list.html', {'professores': professores})

def professor_create(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()
    return render(request, 'sistema_escolar/professor_form.html', {'form': form})

def professor_update(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)
    return render(request, 'sistema_escolar/professor_form.html', {'form': form})

def professor_delete(request, pk):
    professor = get_object_or_404(Professor, pk=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('professor_list')
    return render(request, 'sistema_escolar/professor_confirm_delete.html', {'professor': professor})

@login_required
def professor_dashboard(request):
    return render(request, 'sistema_escolar/professor_dashboard.html')

@login_required
def aluno_dashboard(request):
    return render(request, 'sistema_escolar/aluno_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'sistema_escolar/admin_dashboard.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from usuarios.models import Usuario
from django.urls import reverse

def lista_equipamentos(request):
    equipamentos = Equipamento.objects.select_related('usuario').all()
    return render(request, 'equipamentos/lista.html', {'equipamentos': equipamentos})

def adicionar_equipamento(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        potencia_watts = request.POST.get('potencia_watts', '0').strip() or '0'
        horas_uso_diario = request.POST.get('horas_uso_diario', '0').strip() or '0'
        usuario_id = request.POST.get('usuario')

        tipo = request.POST.get('tipo', 'Desconhecido')  
        status = request.POST.get('status', 'Inativo')

       
        from decimal import Decimal, InvalidOperation
        try:
            potencia = Decimal(potencia_watts)
        except (InvalidOperation, TypeError):
            potencia = Decimal('0')

        try:
            horas = Decimal(horas_uso_diario)
        except (InvalidOperation, TypeError):
            horas = Decimal('0')

        usuario = None
        if usuario_id:
            usuario = get_object_or_404(Usuario, pk=usuario_id)
        else:
           
            return render(request, 'equipamentos/adicionar.html', {
                'usuarios': usuarios,
                'error': 'Selecione um usuário.'
            })

        equipamento = Equipamento.objects.create(
            nome=nome,
            tipo=tipo,
            potencia=potencia,
            horas_uso_diario=horas,
            status=status,
            usuario=usuario
        )
        return redirect(reverse('lista_equipamentos'))

    return render(request, 'equipamentos/adicionar.html', {'usuarios': usuarios})

def editar_equipamento(request,id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        equipamento.nome = request.POST.get('nome', equipamento.nome).strip()

        potencia_watts = request.POST.get('potencia_watts', None)
        horas_uso_diario = request.POST.get('horas_uso_diario', None)

        from decimal import Decimal, InvalidOperation
        if potencia_watts is not None:
            try:
                equipamento.potencia = Decimal(potencia_watts)
            except (InvalidOperation, TypeError):
                pass

        if horas_uso_diario is not None:
            try:
                equipamento.horas_uso_diario = Decimal(horas_uso_diario)
            except (InvalidOperation, TypeError):
                pass

        usuario_id = request.POST.get('usuario')
        if usuario_id:
            equipamento.usuario = get_object_or_404(Usuario, pk=usuario_id)

       
        tipo = request.POST.get('tipo', None)
        if tipo is not None:
            equipamento.tipo = tipo

        status = request.POST.get('status', None)
        if status is not None:
            equipamento.status = status

        equipamento.save()
        return redirect(reverse('lista_equipamentos'))

    return render(request, 'equipamentos/editar.html', {
        'equipamento': equipamento,
        'usuarios': usuarios
    })

def excluir_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamento, id=equipamento_id)
    equipamento.delete()
    return redirect('lista_equipamentos') 


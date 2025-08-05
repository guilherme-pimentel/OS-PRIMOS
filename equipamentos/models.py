from django.db import models
from usuarios.models import Usuario

class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Inativo', 'Inativo'),
        ('Manutenção', 'Manutenção'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, default='Desconhecido')
    potencia = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    horas_uso_diario = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inativo')
    ultima_leitura = models.DateTimeField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} ({self.usuario.nome})'

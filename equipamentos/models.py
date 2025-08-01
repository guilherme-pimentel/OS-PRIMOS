from django.db import models
from usuarios.models import Usuario

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    potencia_watts = models.DecimalField(max_digits=10, decimal_places=2)
    horas_uso_diario = models.DecimalField(max_digits=5, decimal_places=2)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} ({self.usuario.nome})'

from django.db import models
from funcionario.models import Funcionario

class Atividade(models.Model):
    nome = models.CharField(max_length=100)
    hora = models.TimeField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.hora}"
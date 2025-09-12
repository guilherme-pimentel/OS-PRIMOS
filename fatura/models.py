from django.db import models
from matricula.models import Matricula

class Fatura(models.Model):
    data = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    data_vencimento = models.DateField(null=True, blank=True)
    data_pagamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Fatura {self.id} - {self.matricula.aluno.username}"
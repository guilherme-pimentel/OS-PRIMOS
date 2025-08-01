from django.db import models
from leituras.models import Leitura

class Fatura(models.Model):
    data_emissao = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    leitura = models.ForeignKey(Leitura, on_delete=models.CASCADE)
    paga = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.leitura.medidor.numero_serie} - {self.data_emissao}'

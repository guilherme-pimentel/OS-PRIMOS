from django.db import models
from medidores.models import Medidor

class Leitura(models.Model):
    data = models.DateField()
    consumo_kwh = models.DecimalField(max_digits=10, decimal_places=2)
    medidor = models.ForeignKey(Medidor, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.medidor.numero_serie} - {self.data} - {self.consumo_kwh} kWh'

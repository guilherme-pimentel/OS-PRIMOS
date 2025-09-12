from django.db import models
from funcionario.models import Funcionario
from matricula.models import Matricula

class Avaliacao(models.Model):
    data = models.DateField(auto_now_add=True)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name="avaliacoes")
    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    avaliador = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Avaliação de {self.matricula.aluno.username} em {self.data}"

    @property
    def imc(self):
        if self.altura and self.altura > 0:
            return round(self.peso / ((self.altura / 100) ** 2), 2)
        return None
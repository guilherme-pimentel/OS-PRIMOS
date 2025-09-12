from django.db import models
from django.contrib.auth.models import User
from atividade.models import Atividade

class Matricula(models.Model):
    aluno = models.OneToOneField(User, on_delete=models.CASCADE) #
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    atividade = models.ManyToManyField(Atividade) 
    data_matricula = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
     return f"{self.aluno.username} - {', '.join(a.nome for a in self.atividade.all())}"
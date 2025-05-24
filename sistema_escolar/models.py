from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='aluno_sistema_escolar')  # Mudando related_name
    matricula = models.CharField(max_length=20)
    turma = models.ForeignKey('Turma', on_delete=models.SET_NULL, null=True)
    contato = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    serie = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} - {self.serie} - {self.turno}"
    
class Professor(models.Model):
    nome = models.CharField(max_length=150)
    contato = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome
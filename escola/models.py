from django.db import models
from django.contrib.auth.models import User

class Perfil(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    PROFESSOR = 'PROF', 'Professor'
    ALUNO = 'ALUNO', 'Aluno'

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.CharField(max_length=5, choices=Perfil.choices)

    def __str__(self):
        return f'{self.user.username} - {self.perfil}'

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    serie = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nome} - {self.serie} - {self.turno}"

class Professor(models.Model):
    nome = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    contato = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='aluno_escola')  # Mudando related_name
    matricula = models.CharField(max_length=20)
    turma = models.ForeignKey('Turma', on_delete=models.SET_NULL, null=True)
    contato = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nome} ({self.codigo})"

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} : {self.nota}"

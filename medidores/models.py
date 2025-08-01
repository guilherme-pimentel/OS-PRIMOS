from django.db import models
from usuarios.models import Usuario

class Medidor(models.Model):
    numero_serie = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=200)
    data_instalacao = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.numero_serie} - {self.usuario.nome}'

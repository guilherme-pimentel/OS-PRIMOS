from django.db import models
from django.contrib.auth.models import User

class Funcionario(User): 
    cargo = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username  



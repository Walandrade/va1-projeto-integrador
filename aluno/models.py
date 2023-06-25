
from django.db import models


class Aluno(models.Model):
    nome_completo = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    telefone = models.IntegerField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

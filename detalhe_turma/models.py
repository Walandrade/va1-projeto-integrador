from django.db import models

class detalhe_turma(models.Model):
    codigoAluno = models.IntegerField()
    codigoProfessor = models.IntegerField()
    codigoTurma = models.IntegerField()
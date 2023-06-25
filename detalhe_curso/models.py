from django.db import models

class Detalhe_Curso(models.Model):
    codigoCurso = models.IntegerField()
    codigoTurma = models.IntegerField()
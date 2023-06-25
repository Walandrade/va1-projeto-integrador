from django.db import models

class detalhe_disciplina(models.Model):
    codigoCurso = models.IntegerFiel()
    codigoDisciplina = models.IntegerField()

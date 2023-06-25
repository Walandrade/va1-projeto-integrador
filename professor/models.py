from django.db import models

class professor(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    registro = models.CharField(max_length=100)
   

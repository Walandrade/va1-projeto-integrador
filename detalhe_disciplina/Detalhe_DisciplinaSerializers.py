from rest_framework import serializers
from .models import Detalhe_Disciplina


class Detalhe_Disciplina(serializers.ModelSerializer):

    class Meta:
        model = Detalhe_Disciplina
        fields = ['codigoCurso', 'codigoDisciplina']
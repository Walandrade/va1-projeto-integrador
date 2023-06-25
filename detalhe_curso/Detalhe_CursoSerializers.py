from rest_framework import serializers
from .models import Detalhe_Curso


class Detalhe_Curso(serializers.ModelSerializer):

    class Meta:
        model = Detalhe_Curso
        fields = ['codigoCurso', 'codigoTurma']
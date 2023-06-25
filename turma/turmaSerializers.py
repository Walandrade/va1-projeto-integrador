from rest_framework import serializers
from .models import Turma


class Turma(serializers.ModelSerializer):

    class Meta:
        model = Turma
        fields = ['codigo', 'codigoCurso']
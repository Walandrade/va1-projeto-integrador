from rest_framework import serializers
from .models import Detalhe_TurmaSerializers


class Detalhe_TurmaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Detalhe_TurmaSerializers
        fields = ['codigoAluno', 'codigoProfessor', 'codigoTurma']
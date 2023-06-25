from rest_framework import serializers
from .models import Aluno


class Aluno(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        fields = ['nome', 'sexo', 'telefone']
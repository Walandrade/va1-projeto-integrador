from rest_framework import serializers
from .models import Professor


class Professor(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ['nome', 'sexo', 'registro']
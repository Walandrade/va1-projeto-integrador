from rest_framework import serializers
from .models import DisciplinaSerializers


class DisciplinaSerializers(serializers.ModelSerializer):

    class Meta:
        model = DisciplinaSerializers
        fields = ['nome', 'codigo']
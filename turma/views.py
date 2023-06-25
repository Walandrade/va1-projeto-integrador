from rest_framework import generics
from .models import Turma
from .turmaSerializers import TurmaSerializer


class TurmaList(generics.ListCreateAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


class TurmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
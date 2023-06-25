from rest_framework import generics
from .models import Detalhe_Disciplina
from .Detalhe_DisciplinaSerializers import Detalhe_DisciplinaSerializer


class Detalhe_DisciplinaList(generics.ListCreateAPIView):
    queryset = Detalhe_Disciplina.objects.all()
    serializer_class = Detalhe_DisciplinaSerializer


class Detalhe_DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detalhe_Disciplina.objects.all()
    serializer_class = Detalhe_DisciplinaSerializer
from rest_framework import generics
from .models import Detalhe_Turma
from .Detalhe_TurmaSerializers import Detalhe_TurmaSerializer


class Detalhe_TurmaList(generics.ListCreateAPIView):
    queryset = Detalhe_Turma.objects.all()
    serializer_class = Detalhe_TurmaSerializer


class Detalhe_TurmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detalhe_Turma.objects.all()
    serializer_class = Detalhe_TurmaSerializer
# Create your views here.

from rest_framework import generics
from .models import Detalhe_curso
from .Detalhe_CursoSerializers import Detalhe_cursoSerializer


class Detalhe_cursoList(generics.ListCreateAPIView):
    queryset = Detalhe_curso.objects.all()
    serializer_class = Detalhe_cursoSerializer


class Detalhe_cursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detalhe_curso.objects.all()
    serializer_class = Detalhe_cursoSerializer
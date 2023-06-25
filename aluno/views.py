from rest_framework import viewsets
from .models import Aluno
from .AlunoSerializers import AlunoSerializer


class AlunoView(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

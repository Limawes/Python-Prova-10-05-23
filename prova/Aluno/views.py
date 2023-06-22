from rest_framework import viewsets
from .models import Aluno
from Aluno.alunoserializer import AlunoSerializer

class AlunoView(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
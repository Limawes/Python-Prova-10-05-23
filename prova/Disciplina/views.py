from rest_framework import viewsets
from .models import Disciplina
from Disciplina.disciplinaserializer import DisciplinaSerializer

class DisciplinaView(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
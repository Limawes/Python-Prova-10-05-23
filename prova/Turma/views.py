from rest_framework import viewsets
from .models import Turma
from Turma.turmaserializer import TurmaSerializer

class TurmaView(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
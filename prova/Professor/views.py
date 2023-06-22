from rest_framework import viewsets
from .models import Professor
from Professor.professorserializer import ProfessorSerializer

class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
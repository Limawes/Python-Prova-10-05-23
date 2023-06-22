from rest_framework import viewsets
from .models import Curso
from Curso.cursoserializer import CursoSerializer

class CursoView(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
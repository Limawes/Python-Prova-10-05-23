from rest_framework import viewsets
from .models import DetalheCurso
from DetalheCurso.detalheCursoserializer import DetalheCursoSerializer

class DetalheCursoView(viewsets.ModelViewSet):
    queryset = DetalheCurso.objects.all()
    serializer_class = DetalheCursoSerializer
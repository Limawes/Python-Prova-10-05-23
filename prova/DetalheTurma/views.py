from rest_framework import viewsets
from .models import DetalheTurma
from DetalheTurma.detalheTurmaserializer import DetalheTurmaSerializer

class DetalheTurmaView(viewsets.ModelViewSet):
    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaSerializer
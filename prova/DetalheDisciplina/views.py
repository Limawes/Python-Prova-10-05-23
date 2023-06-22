from rest_framework import viewsets
from .models import DetalheDisciplina
from DetalheDisciplina.detalheDisciplinaserializer import DetalheDisciplinaSerializer

class DetalheDisciplinaView(viewsets.ModelViewSet):
    queryset = DetalheDisciplina.objects.all()
    serializer_class = DetalheDisciplinaSerializer
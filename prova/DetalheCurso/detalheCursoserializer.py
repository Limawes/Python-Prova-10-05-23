from rest_framework import serializers

from DetalheCurso.models import DetalheCurso

class DetalheCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheCurso
        fields = [
            'codigoCurso',
            'codigoTurma',
        ]
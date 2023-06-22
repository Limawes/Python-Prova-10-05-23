from rest_framework import serializers

from Aluno.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Aluno
        fields =[
            'nome',
            'sexo',
            'matricula',
            'dataNascimento',
        ]
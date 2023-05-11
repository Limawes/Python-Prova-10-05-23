from django.db import models

# Create your models here.

class DetalheTurma(models.Model):
    
    codigoAluno = models.IntegerField(max_length=100)
    codigoProfessor = models.IntegerField(max_length=100)
    codigoTurma = models.IntegerField(max_length=100)
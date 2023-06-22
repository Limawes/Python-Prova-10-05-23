from django.db import models

# Create your models here.

class DetalheTurma(models.Model):
    
    codigoAluno = models.IntegerField()
    codigoProfessor = models.IntegerField()
    codigoTurma = models.IntegerField()
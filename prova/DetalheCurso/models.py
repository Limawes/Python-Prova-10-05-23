from django.db import models

# Create your models here.

class DetalheCurso(models.Model):
    
    codigoCurso = models.IntegerField(max_length=100)
    codigoTurma = models.IntegerField(max_length=100)
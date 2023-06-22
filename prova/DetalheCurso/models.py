from django.db import models

# Create your models here.

class DetalheCurso(models.Model):
    
    codigoCurso = models.IntegerField()
    codigoTurma = models.IntegerField()
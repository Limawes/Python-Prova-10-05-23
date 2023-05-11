from django.db import models

# Create your models here.

class Turma(models.Model):
    
    codigo = models.CharField(max_length=100)
    codigoCurso = models.CharField(max_length=100)
from django.db import models

# Create your models here.

class DetalheDisciplina(models.Model):
    
    codigoCurso = models.IntegerField(max_length=100)
    codigoDisciplina = models.IntegerField(max_length=100)
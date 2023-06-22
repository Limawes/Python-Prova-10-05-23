from django.db import models

# Create your models here.

class DetalheDisciplina(models.Model):
    
    codigoCurso = models.IntegerField()
    codigoDisciplina = models.IntegerField()
# Generated by Django 4.2 on 2023-06-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DetalheCurso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalhecurso',
            name='codigoCurso',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detalhecurso',
            name='codigoTurma',
            field=models.IntegerField(),
        ),
    ]

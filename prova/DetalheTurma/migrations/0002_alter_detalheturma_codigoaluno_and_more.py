# Generated by Django 4.2 on 2023-06-22 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DetalheTurma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalheturma',
            name='codigoAluno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detalheturma',
            name='codigoProfessor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='detalheturma',
            name='codigoTurma',
            field=models.IntegerField(),
        ),
    ]

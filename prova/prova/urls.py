"""prova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Aluno.views import AlunoView
from Curso.views import CursoView
from DetalheCurso.views import DetalheCursoView
from DetalheDisciplina.views import DetalheDisciplinaView
from DetalheTurma.views import DetalheTurmaView
from Disciplina.views import DisciplinaView
from Professor.views import ProfessorView
from Turma.views import TurmaView

rotas = routers.DefaultRouter()
rotas.register(r'aluno', AlunoView, basename='Aluno'),
rotas.register(r'curso', CursoView, basename='Curso'),
rotas.register(r'detalheCurso', DetalheCursoView, basename='DetalheCurso'),
rotas.register(r'detalheDisciplina', DetalheDisciplinaView, basename='DetalheDisciplina'),
rotas.register(r'detalheTurma', DetalheTurmaView, basename='DetalheTurma'),
rotas.register(r'disciplina', DisciplinaView, basename='Disciplina'),
rotas.register(r'professor', ProfessorView, basename='Professor'),
rotas.register(r'turma', TurmaView, basename='Turma'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls)),
]

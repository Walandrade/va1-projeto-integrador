"""
URL configuration for va2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers
from django.urls import include, path
from aluno.views import AlunoView

rotas = routers.DefaultRouter()
rotas.register(r'aluno', AlunoView, basename='Aluno'),
rotas.register(r'curso', AlunoView, basename='Curso'),
rotas.register(r'detalhe_curso', AlunoView, basename='detalhe_curso'),
rotas.register(r'detalhe_disciplina', AlunoView, basename='detalhe_disciplina'),
rotas.register(r'detalhe_turma', AlunoView, basename='detalhe_turma'),
rotas.register(r'disciplina', AlunoView, basename='disciplina'),
rotas.register(r'professor', AlunoView, basename='professor'),
rotas.register(r'turma', AlunoView, basename='turma'),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(rotas.urls)),
]

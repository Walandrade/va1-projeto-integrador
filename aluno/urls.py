from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from aluno import views

urlpatterns = [
    path('alunos/', views.PersonList.as_view()),
    path('alunos/<int:pk>/', views.PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
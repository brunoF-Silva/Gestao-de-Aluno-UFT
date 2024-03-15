from django.urls import path

from . import views

urlpatterns = [
  path('', views.home),
  path('alunos/', views.AlunoListView.as_view(), name='listar_alunos'),
  path("about/", views.AboutView.as_view()),
  path("profile/<int:pk>", views.AlunoDetailView.as_view()),
  path('cadastrar/', views.AlunoCreateView.as_view(), name='criar_aluno'),
  path('mesmo-curso/', views.ListaAlunosMesmoCursoView.as_view(), name='alunos-mesmo-curso'),

]
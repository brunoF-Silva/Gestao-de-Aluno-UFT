from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('cadastrar/', views.AlunoCreateView.as_view(), name='criar_aluno'),
  path('visualizarDados/', views.VisualizarDadosView.as_view(), name='visualizarDados'),
  path("visualizarDados/perfil/<uuid:pk>", views.AlunoDetailView.as_view(), name='perfil-aluno'),
  path("visualizarDados/editarPerfil/<uuid:pk>", views.editarAlunoView.as_view(), name='editar-perfil-aluno'),
  path('mesmo-curso/', views.ListaAlunosMesmoCursoView.as_view(), name='alunos-mesmo-curso'),
]
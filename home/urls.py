from django.urls import path

from . import views

urlpatterns = [
  path('alunos/', views.AlunoListView.as_view(), name='listar_alunos'),
  path("about/", views.AboutView.as_view()),
  path('cadastrar/', views.AlunoCreateView.as_view(), name='criar_aluno'),
  path('mesmo-curso/', views.ListaAlunosMesmoCursoView.as_view(), name='alunos-mesmo-curso'),
  path('', views.IndexView.as_view(), name='index'),
  path('visualizarDados/', views.VisualizarDadosView.as_view(), name='visualizarDados'),
  path('methods/', views.MethodsView.as_view(), name='methods'),
  path("visualizarDados/perfil/<uuid:pk>", views.AlunoDetailView.as_view(), name='perfil-aluno'),

]
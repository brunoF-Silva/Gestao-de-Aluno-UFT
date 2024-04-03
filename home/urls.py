from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexTemplateView.as_view(), name='index'),
  path('cadastrar/', views.AlunoCreateView.as_view(), name='cadastrarAluno'),
  path('alunos/', views.VisualizarAlunosListView.as_view(), name='alunos'),
  path("alunos/perfil/<uuid:pk>", views.AlunoDetailView.as_view(), name='perfilAluno'),
  path("alunos/editar/<uuid:pk>", views.EditarAlunoDetailView.as_view(), name='editarPerfilAluno'),
]
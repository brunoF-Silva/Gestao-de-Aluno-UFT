from django.urls import path

from .views import *

urlpatterns = [
  path('', IndexTemplateView.as_view(), name='index'),
  path('cadastrar/', AlunoCreateView.as_view(), name='cadastrarAluno'),
  path('alunos/', VisualizarAlunosListView.as_view(), name='alunos'),
  path("alunos/perfil/<uuid:pk>", AlunoDetailView.as_view(), name='perfilAluno'),
  path("alunos/editar/<uuid:pk>", EditarAlunoDetailView.as_view(), name='editarPerfilAluno'),
]
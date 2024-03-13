from django.urls import path

from . import views

urlpatterns = [
  path('', views.home),
  path('cadastrar/', views.cadastrar),
  path('alunos', views.AlunoListView.as_view())
]
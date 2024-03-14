from django.urls import path

from . import views

urlpatterns = [
  path('', views.home),
  path('cadastrar/', views.cadastrar),
  path('alunos/', views.AlunoListView.as_view()),
  path("about/", views.AboutView.as_view()),
  path("profile/<int:pk>", views.AlunoDetailView.as_view())
]
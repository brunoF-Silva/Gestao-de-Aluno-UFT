from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from home.models import Aluno

# Create your views here.

def home(request):
  print('home')
  return render(
    request,
    'home/index.html'
  )

def cadastrar(request):
  print('cadastro')
  return HttpResponse('cadastrar')

class AlunoListView(ListView):
  model = Aluno
  template_name = "home/teste.html"

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView

from home.models import Aluno
from home.models import Curso

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

class AboutView(TemplateView):
    template_name = "about.html"

class AlunoDetailView(DetailView):
   model = Aluno

   def get_context_data(self, **kwargs):
      pk = self.kwargs.get('pk')
      aluno = Aluno.objects.get(id_aluno=pk)
      context = super().get_context_data(**kwargs)
      context['curso'] = Curso.objects.get(id_curso=aluno.curso.id_curso)
      return context
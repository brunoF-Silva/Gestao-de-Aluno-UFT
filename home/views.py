from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse_lazy
from datetime import datetime



from home.models import Aluno, Curso
from .forms import AlunoForm

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
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['curso'] = Curso.objects.all()

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
   
class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'home/cadastro.html'
    success_url = reverse_lazy('alunos-mesmo-curso')

    def form_valid(self, form):
        # Gerar matrícula automaticamente
        now = datetime.now()
        year = now.year
        half_year = 1 if now.month <= 6 else 2
        alunos_no_ano = Aluno.objects.filter(matricula__startswith=str(year)).count()
        incremental_digit = str(alunos_no_ano + 1).zfill(4)
        matricula = f'{year}{half_year}{incremental_digit}'

        # Adicionar matrícula ao formulário
        form.instance.matricula = matricula

        return super().form_valid(form)
    
class ListaAlunosMesmoCursoView(ListView):
    template_name = 'home/alunos_mesmo_curso.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        # Obter o último aluno cadastrado
        ultimo_aluno = Aluno.objects.latest('id_aluno')

        # Filtrar todos os alunos no mesmo curso do último aluno cadastrado
        alunos_mesmo_curso = Aluno.objects.filter(curso=ultimo_aluno.curso)

        return alunos_mesmo_curso

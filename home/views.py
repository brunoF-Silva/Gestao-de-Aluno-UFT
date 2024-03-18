from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView, CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from datetime import datetime
from django.db.models import Count




from home.models import Aluno, Curso
from .forms import AlunoForm, FiltroForm

# Create your views here.

def home(request):
  print('home')
  return render(
    request,
    'home/index.html'
  )


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
      aluno = Aluno.objects.get(id=pk)
      context = super().get_context_data(**kwargs)
      context['curso'] = Curso.objects.get(id=aluno.curso.id)
      return context
   
    
class IndexView(TemplateView):
    template_name = 'index.html'

class ListaAlunosMesmoCursoView(ListView):
    template_name = 'home/alunos_mesmo_curso.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        # Obter o último aluno cadastrado
        ultimo_aluno = Aluno.objects.latest('id')

        # Filtrar todos os alunos no mesmo curso do último aluno cadastrado
        alunos_mesmo_curso = Aluno.objects.filter(curso=ultimo_aluno.curso)

        return alunos_mesmo_curso
    
class VisualizarDadosView(ListView, FormView):
    template_name='home/visualizarDados.html'
    model =  Aluno
    context_object_name = 'alunos'
    form_class = FiltroForm
    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["cursos"] = Curso.objects.all()
      return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            curso_selecionado = form.cleaned_data['curso']
            campus_selecionado = form.cleaned_data['campus']
            if curso_selecionado and campus_selecionado:
                queryset = Aluno.objects.filter(curso=curso_selecionado, campus=campus_selecionado)
        return queryset

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

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

class MethodsView(ListView):
    model = Aluno
    template_name = 'home/methodTest.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        # Retorna apenas os alunos do curso de "Engenharia"
        return Aluno.objects.values('curso')
    
"""
from .models import Aluno

# Retorna todos os objetos do modelo Aluno
alunos = Aluno.objects.all()

from .models import Aluno

# Retorna um único objeto que atende aos critérios especificados
aluno = Aluno.objects.get(id=1)  # Obtém o aluno com ID igual a 1

from .models import Aluno

# Retorna um queryset contendo todos os objetos que atendem aos critérios especificados
alunos = Aluno.objects.filter(curso='Engenharia')  # Obtém todos os alunos do curso de Engenharia

from .models import Aluno

# Retorna um queryset contendo todos os objetos que não atendem aos critérios especificados
alunos = Aluno.objects.exclude(curso='Engenharia')  # Obtém todos os alunos que não são do curso de Engenharia

from .models import Aluno

# Ordena os resultados do queryset com base nos critérios especificados
alunos = Aluno.objects.all().order_by('nome')  # Obtém todos os alunos ordenados pelo nome

from django.db.models import Count
from .models import Aluno

# Adiciona contagem de alunos por curso ao queryset
alunos_por_curso = Aluno.objects.values('curso').annotate(total=Count('curso'))

from .models import Aluno

# Retorna um queryset contendo dicionários em vez de objetos completos
dados_alunos = Aluno.objects.values('nome', 'curso')  # Obtém apenas os nomes e cursos dos alunos

from .models import Aluno

# Remove duplicatas do queryset resultante
alunos_distintos = Aluno.objects.values('curso').distinct()  # Obtém os cursos distintos dos alunos

from .models import Aluno

# Retorna o número de objetos no queryset
total_alunos = Aluno.objects.count()  # Obtém o número total de alunos

from .models import Aluno

# Retorna True se pelo menos um objeto atender aos critérios especificados no queryset
aluno_existe = Aluno.objects.filter(curso='Medicina').exists()  # Verifica se há alunos no curso de Medicina

from .models import Aluno

# Cria um novo objeto do modelo e o salva no banco de dados
novo_aluno = Aluno.objects.create(nome='João', curso='Engenharia')  # Cria um novo aluno

from .models import Aluno

# Atualiza os valores de um ou mais objetos do queryset
Aluno.objects.filter(curso='Engenharia').update(curso='Física')  # Atualiza o curso de todos os alunos de Engenharia para Física
"""

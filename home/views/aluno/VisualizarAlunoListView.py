from django.views.generic.list import ListView
from django.views.generic import FormView
from home.models import Aluno, Curso, Campus
from home.forms import DesvincularForm, FiltroForm
from django.http import QueryDict
from urllib.parse import urlencode
from django.db.models import F

class VisualizarAlunosListView(ListView, FormView):
    template_name='home/VisualizarAlunos.html'
    model =  Aluno
    # context_object_name = 'alunos'
    form_class = FiltroForm
    paginate_by = 10
    querysetGeral = []
    curso = ''
    campus = ''
    salvaQueryset = {}

    def post(self, request, *args, **kwargs):
        print(request.POST.get('campoOculto'))
        aluno = Aluno.objects.get(matricula = request.POST.get('campoOculto'))
        aluno.situacao = request.POST.get('situacao')
        aluno.save()
        return super().get(request, *args, **kwargs)   
    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["cursos"] = Curso.objects.all()
      context['desvincularForm'] = DesvincularForm()
      
      form = self.form_class(self.request.GET or None)
      form_data = form.data.dict() if form.is_bound else {}
      query_dict = QueryDict(mutable=True)
      query_dict.update(form_data)
      context['query_params'] = urlencode({k: v for k, v in query_dict.items() if not k.startswith("page")})
      context["alunosTotal"] = self.querysetGeral
      context["curso"] = self.curso
      context["campus"] = self.campus
      return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET or None)  # Usando GET para obter os parâmetros do formulário
        queryset = Aluno.objects.filter()
        queryset = queryset.order_by('nome') 
        print('OLHA SOOOOOOOOO')
        self.curso = None
        self.campus = None

        
        if form.is_valid():
            cursoSelecionado = form.cleaned_data['curso']
            campusSelecionado = form.cleaned_data['campus']
            pesquisa = form.cleaned_data['pesquisa']
            

            if cursoSelecionado == '':
                cursoSelecionado = None
                
            if pesquisa:
                queryset = Aluno.objects.filter(matricula = pesquisa)
                queryset = queryset.order_by('nome') 

            else:
                ids = []
                queryset = []
                self.curso = cursoSelecionado
                self.campus = campusSelecionado

                if cursoSelecionado is None and campusSelecionado is None:
                    queryset = Aluno.objects.filter()
                    queryset = queryset.order_by('nome') 

                elif cursoSelecionado and campusSelecionado is None:
                    ids =  Curso.objects.filter(nome__icontains = cursoSelecionado).values('id')
                    ids = [e['id'] for e in ids]
                    print(ids)
                    queryset = Aluno.objects.filter(curso_id__in=ids)
                    queryset = queryset.order_by('-matricula') 
                    
                elif cursoSelecionado is None and campusSelecionado:
                    # cursos = Curso.objects.all()
                    # cursos = cursos.filter(campus__campus=campusSelecionado)
                    ids = Campus.objects.filter(campus__icontains = campusSelecionado).values('id')
                    print(ids)
                    
                    ids = [e['id'] for e in ids]

                    print(ids)
                    cursos = Curso.objects.filter(campus__in = ids)
                    print(cursos)
                    queryset = Aluno.objects.filter(curso__in=cursos)
                    queryset = queryset.order_by('-matricula') 

                elif campusSelecionado and cursoSelecionado:
                    cursos =  Curso.objects.filter(nome__icontains = cursoSelecionado)
                    ids = Campus.objects.filter(campus__icontains = campusSelecionado).values('id')
                    ids = [e['id'] for e in ids]
                    
                    print(ids)

                    cursos = cursos.filter(campus__in = ids)
                    queryset =  Aluno.objects.filter(curso__in = cursos)
                    queryset = queryset.order_by('-matricula')

        queryset = queryset.annotate(index=F('id'))
        self.salvaQueryset = queryset

        # if cursoSelecionado and campusSelecionado:
        #    for index, item in (reversed(queryset), 1):
        #         item.index = index
        # else:
        for index, item in enumerate(reversed(queryset), 1):
            item.index = index
        
        self.querysetGeral = queryset.count()
        return queryset
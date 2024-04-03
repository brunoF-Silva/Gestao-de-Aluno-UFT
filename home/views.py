from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView, CreateView, TemplateView, FormView
from django.urls import reverse_lazy
from datetime import datetime
from home.models import Aluno, Curso, Campus
from .forms import AlunoForm, DesvincularForm, FiltroForm, EditarAlunoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from django.http import QueryDict
from urllib.parse import urlencode



class IndexTemplateView(TemplateView):
    model = Aluno
    template_name = 'home/Index.html'
    context_object_name = 'alunos'
    form_class = FiltroForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alunosVinculados = Aluno.objects.filter(situacao='Vinculado')
        alunosFormados = Aluno.objects.filter(situacao='Formado')
        alunosJubilados = Aluno.objects.filter(situacao='Jubilado')
        alunosEvadidos = Aluno.objects.filter(situacao='Evadido')

        totalAlunos = Aluno.objects.all()
        totalAlunosCount = totalAlunos.count()
        amarela = Aluno.objects.filter(raca = 'Amarela').count()
        branca = Aluno.objects.filter(raca = 'Branca').count()
        indigena = Aluno.objects.filter(raca = 'Indigena').count()
        print('indigena',indigena)
        parda = Aluno.objects.filter(raca = 'Parda').count()
        preta = Aluno.objects.filter(raca = 'Preta').count()
        
        masculino = Aluno.objects.filter(sexo = 'M').count()
        feminino = Aluno.objects.filter(sexo = 'F').count()
        outro = Aluno.objects.filter(sexo = 'O').count()

        
        totalSexo = masculino + feminino + outro
        masculinoProp = int(100 * (masculino / totalSexo))
        femininoProp = int(100 * (feminino / totalSexo))
        outroProp = int(100 * (outro / totalSexo))
        
        anos = []
        for aluno in totalAlunos:
            ano = aluno.matricula[:5]
            if ano in anos:
                continue
            else:
                anos.append(ano)
                
        anos = sorted(anos)
        
        print(anos)
        
        anoQtd = {}
        for ano in anos:
            cont = 0
            for aluno in totalAlunos:
                
                if aluno.matricula[:5] == ano:
                    print('entrou')
                    cont+=1
                anoQtd[ano] = cont
        print(anoQtd)
        campos = list(anoQtd.keys())

        valores = list(anoQtd.values())
        print(campos,valores)
        
        context = {
            'amarela': '{:.2f}'.format(100 *(amarela / totalAlunosCount)),
            'branca': '{:.2f}'.format(100 *(branca / totalAlunosCount)),
            'indigena': '{:.2f}'.format(100 *(indigena / totalAlunosCount)),
            'parda': '{:.2f}'.format(100 *(parda / totalAlunosCount)),
            'preta': '{:.2f}'.format(100 *(preta / totalAlunosCount)),
            'totalAlunosVinculados': alunosVinculados.count(),
            'totalAlunosFormados': alunosFormados.count(),
            'totalAlunosJubilados': alunosJubilados.count(),
            'totalAlunosEvadidos': alunosEvadidos.count(),
            'masculino': masculino,
            'feminino': feminino,
            'outro': outro,
            'masculinoProp' : masculinoProp,
            'femininoProp' : femininoProp,
            'outroProp' : outroProp,
            'camposJson': json.dumps(campos),
            'valoresJson': json.dumps(valores),
        }

        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            cursoSelecionado = form.cleaned_data['curso']
            campusSelecionado = form.cleaned_data['campus']
            if cursoSelecionado and campusSelecionado:
                queryset = Aluno.objects.filter(curso=cursoSelecionado, campus=campusSelecionado)
        return queryset

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

class AlunoCreateView(CreateView):
    form_class = AlunoForm
    template_name = 'home/Cadastrar.html'
    model = Aluno
    
    def dispatch(self, request, *args, **kwargs):
        self.request.session.setdefault('formularioEnviado', False)
        print("1 ", self.request.session['formularioEnviado'])
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formularioEnviado'] = self.request.session['formularioEnviado']
        print("2 ", self.request.session['formularioEnviado'])
        return context

    def form_valid(self, form):
        hoje = datetime.now()
        ano = hoje.year
        semestre = 1 if hoje.month <= 6 else 2
        alunosNoAno = Aluno.objects.filter(matricula__startswith=str(f'{ano}{semestre}')).count()
        incremental = str(alunosNoAno + 1).zfill(4)
        matricula = f'{ano}{semestre}{incremental}'

        form.instance.matricula = matricula
        form.instance.situacao = 'Vinculado'

        self.request.session['formularioEnviado'] = True
        print('3 ', self.request.session['formularioEnviado'])

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('criarAluno')


# class CadastrarAlunosView(CreateView):
#     form_class = AlunoForm
#     template_name = 'home/cadastro.html'
#     success_url = reverse_lazy('alunos-mesmo-curso')
#     model = Aluno
#     formulario_enviado = False

#     def form_valid(self, form):
#         hoje = datetime.now()
#         ano = hoje.year
#         semestre = 1 if hoje.month <= 6 else 2
#         alunosNoAno = Aluno.objects.filter(matricula__startswith=str(f'{ano}{semestre}')).count()
#         incremental = str(alunosNoAno + 1).zfill(4)
#         matricula = f'{ano}{semestre}{incremental}'

#         form.instance.matricula = matricula

#         form.instance.situacao = 'Vinculado'
#         return super().form_valid(form)
    
# def mostraPopUp(request):
#     formularioEnviado = False
#     if request.method == 'POST':
#         # Processamento do formulário aqui
#         # ...
#         formularioEnviado = True  # Atualiza a variável para True após o envio do formulário
    
#     return render(request, 'meu_template.html', {'formulario_enviado': formularioEnviado})

    

class AlunoDetailView(DetailView):
   model = Aluno
   template_name = "home/Perfil.html"
   context_object_name = 'aluno'
   form_class = AlunoForm


   def get_context_data(self, **kwargs):
      pk = self.kwargs.get('pk')
      aluno = Aluno.objects.get(id=pk)
      context = super().get_context_data(**kwargs)
      context['cursos'] = Curso.objects.all()
      return context
      
class EditarAlunoDetailView(DetailView):
    model = Aluno
    template_name = "home/EditarPerfil.html"
    context_object_name = 'aluno'
    form_class = EditarAlunoForm


    def get_context_data(self, **kwargs):
        # pk = self.kwargs.get('pk')
        # aluno = Aluno.objects.get(id=pk)
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        aluno = self.get_object()
        print(aluno)
        form = self.form_class(request.POST, request.FILES, instance=aluno)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            print('UUEEEE')
            form.save()
            return HttpResponseRedirect(reverse('editarPerfilAluno', kwargs={'pk': aluno.pk}))
        return super().get(request, *args, **kwargs)   

class ListarAlunosMesmoCursoView(ListView):
    template_name = 'home/alunos_mesmo_curso.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        # Obter o último aluno cadastrado
        ultimo_aluno = Aluno.objects.latest('id')

        # Filtrar todos os alunos no mesmo curso do último aluno cadastrado
        alunos_mesmo_curso = Aluno.objects.filter(curso=ultimo_aluno.curso)

        return alunos_mesmo_curso
    
# class VisualizarDadosView(ListView, FormView):
#     template_name='home/visualizarDados.html'
#     model =  Aluno
#     context_object_name = 'alunos'
#     form_class = FiltroForm
    
#     def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs)
#       context["cursos"] = Curso.objects.all()
#       return context
    
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         form = self.form_class(self.request.POST or None)
#         if form.is_valid():


#             cursoSelecionado = form.cleaned_data['curso']
#             campusSelecionado = form.cleaned_data['campus']
#             pesquisa = form.cleaned_data['pesquisa']
            
#             print(cursoSelecionado)
#             print(campusSelecionado)

#             if cursoSelecionado is '':
#                 cursoSelecionado = None
                
#             if pesquisa:
#                 queryset = Aluno.objects.filter(matricula = pesquisa)
#             else:
#                 ids = []
#                 queryset = []
#                 if cursoSelecionado and campusSelecionado is None:
#                     print('Entrou 1')
#                     ids =  Curso.objects.filter(nome__icontains = cursoSelecionado).values('id')
#                     ids = [e['id'] for e in ids]
#                     print(ids)
#                     queryset = Aluno.objects.filter(curso_id__in=ids)

#                 elif cursoSelecionado is None and campusSelecionado:
#                     print('Entrou 2')
#                     print(campusSelecionado)

#                     # cursos = Curso.objects.all()
#                     # cursos = cursos.filter(campus__campus=campusSelecionado)
#                     ids = Campus.objects.filter(campus__icontains = campusSelecionado).values('id')
#                     print(ids)
                    
#                     ids = [e['id'] for e in ids]

#                     print(ids)
#                     cursos = Curso.objects.filter(campus__in = ids)
#                     print(cursos)
#                     queryset = Aluno.objects.filter(curso__in=cursos)
#                 elif campusSelecionado and cursoSelecionado:
#                     print('Entrou 3')

#                     cursos =  Curso.objects.filter(nome__icontains = cursoSelecionado)
#                     ids = Campus.objects.filter(campus__icontains = campusSelecionado).values('id')
#                     ids = [e['id'] for e in ids]

#                     cursos = cursos.filter(campus__in = ids)
#                     queryset =  Aluno.objects.filter(curso__in = cursos)
                    
#                 elif campusSelecionado is None and cursoSelecionado is None:
#                     print("NOOOOOOOONNNNNNEEEE")
#         return queryset




class VisualizarAlunosListView(ListView, FormView):
    template_name='home/VisualizarAlunos.html'
    model =  Aluno
    # context_object_name = 'alunos'
    form_class = FiltroForm
    paginate_by = 10
    # query_dict = QueryDict(mutable=True)
    # dados_iniciais = urlencode({k: v for k, v in query_dict.items()})
    # print('DADOS INICIAIS', dados_iniciais, 'Yeah')
    # form = FiltroForm(initial=dados_iniciais)

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
      print('!!!!!!!',context)
      return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET or None)  # Usando GET para obter os parâmetros do formulário
        queryset = Aluno.objects.filter()
        queryset = queryset.order_by('nome') 
        
        if form.is_valid():
            cursoSelecionado = form.cleaned_data['curso']
            campusSelecionado = form.cleaned_data['campus']
            pesquisa = form.cleaned_data['pesquisa']
            

            if cursoSelecionado == '':
                cursoSelecionado = None
                
            print(cursoSelecionado)
            print(campusSelecionado)
            if pesquisa:
                queryset = Aluno.objects.filter(matricula = pesquisa)
                queryset = queryset.order_by('nome') 

            else:
                print('vamos começar')
                ids = []
                queryset = []

                if cursoSelecionado is None and campusSelecionado is None:
                    queryset = Aluno.objects.filter()
                    queryset = queryset.order_by('nome') 
                elif cursoSelecionado and campusSelecionado is None:
                    print('Entrou 1')
                    ids =  Curso.objects.filter(nome__icontains = cursoSelecionado).values('id')
                    ids = [e['id'] for e in ids]
                    print(ids)
                    queryset = Aluno.objects.filter(curso_id__in=ids)
                    queryset = queryset.order_by('-matricula') 

                    
                elif cursoSelecionado is None and campusSelecionado:
                    print('Entrou 2')
                    print(campusSelecionado)

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
                    print('Entrou 3')

                    cursos =  Curso.objects.filter(nome__icontains = cursoSelecionado)
                    ids = Campus.objects.filter(campus__icontains = campusSelecionado).values('id')
                    ids = [e['id'] for e in ids]
                    
                    print(ids)

                    cursos = cursos.filter(campus__in = ids)
                    queryset =  Aluno.objects.filter(curso__in = cursos)
                    queryset = queryset.order_by('-matricula') 

                    
        # print(queryset)
        return queryset
    

    # def post(self, request, *args, **kwargs):
    #     self.object_list = self.get_queryset()
    #     context = self.get_context_data(object_list=self.object_list)
    #     return self.render_to_response(context)
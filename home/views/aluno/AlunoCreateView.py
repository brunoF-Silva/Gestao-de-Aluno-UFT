from django.views.generic import CreateView
from django.urls import reverse_lazy
from datetime import datetime
######
from home.models import Aluno
from home.forms import AlunoForm

class AlunoCreateView(CreateView):
    form_class = AlunoForm
    template_name = 'home/Cadastrar.html'
    model = Aluno
    formularioEnviado = False

    # def dispatch(self, request, *args, **kwargs):
    #     self.request.session.setdefault('formularioEnviado', False)
    #     print("1 ", self.request.session['formularioEnviado'])
    #     return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("2 !!!!!!!!!!!", self.request.session['formularioEnviado'])
        context['formularioEnviado'] = self.formularioEnviado
        AlunoCreateView.formularioEnviado = False
        return context

    def form_valid(self, form):
        AlunoCreateView.formularioEnviado = True
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
        print('4-----------')
        return reverse_lazy('cadastrarAluno')
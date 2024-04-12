from django.views.generic import DetailView
########
from home.models import Aluno, Curso
from home.forms.aluno import AlunoForm



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
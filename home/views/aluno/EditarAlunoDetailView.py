from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
##########
from home.models import Aluno, Curso
from home.forms.aluno import EditarAlunoForm

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

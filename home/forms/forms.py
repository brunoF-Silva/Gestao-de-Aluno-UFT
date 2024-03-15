from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'  # Todos os campos do modelo Aluno serão incluídos no formulário

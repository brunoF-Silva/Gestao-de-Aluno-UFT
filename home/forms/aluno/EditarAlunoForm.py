from django import forms
from home.models import Aluno

class EditarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        exclude = ['id','matricula','foto', 'dataDeNasc', 'cpf', 'formaDeIngresso']

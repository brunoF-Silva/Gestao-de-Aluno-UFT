from django import forms
from home.models import Aluno

class AlunoForm(forms.ModelForm):
    dataDeNasc = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )
    class Meta:
        model = Aluno
        field = '__all__'
        exclude = ['situacao', 'matricula',]
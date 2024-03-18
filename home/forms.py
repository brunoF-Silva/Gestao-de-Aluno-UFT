# forms.py
from django import forms
from .models import Aluno, Curso, Campus
from datetime import datetime
from django.shortcuts import render


class AlunoForm(forms.ModelForm):
    data_de_nasc = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Aluno
        exclude = ['situacao', 'matricula']

# class FiltroForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)
#     from django import forms

#     def __init__(self, *args, **kwargs):
#         super(FiltroForm, self).__init__(*args, **kwargs)
#         # Obtém todos os cursos disponíveis e define as escolhas do campo select
#         self.fields['classificacao']  = forms.ChoiceField(choices=self.get_classificacao())       
#         self.fields['campos'] = forms.ChoiceField(choices=self.get_choices())
        

#     def get_choices(self):
#         cursos = Curso.objects.all()
#         # Cria uma lista de tuplas com os valores 'id' e 'nome' dos cursos
#         return [(curso.id_curso, curso.nome) for curso in cursos]
    
#     def get_classificacao(self):
#         cursos = Curso.objects.all()
#         # Cria uma lista de tuplas com os valores 'id' e 'nome' dos cursos
#         return [(curso.id_curso, curso.classificacao) for curso in cursos]
    
from django import forms
from .models import Curso

class FiltroForm(forms.Form):
    # classificacao = forms.ChoiceField(label="Classificação do Curso: ", choices=(('', '-----'), ('Bacharelado', 'Bacharelado'), ('Tecnologo', 'Tecnólogo'), ('Licenciatura', 'Licenciatura')), required=False)
    curso = forms.ModelChoiceField(label="Curso: ", queryset=Curso.objects.all(), required=False)
    campus = forms.ModelChoiceField(label="Campus: ", queryset=Campus.objects.all(), required=False)



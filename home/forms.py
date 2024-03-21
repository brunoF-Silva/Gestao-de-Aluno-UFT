# forms.py
from django import forms
from .models import Aluno, Curso, Campus
from datetime import datetime
from django.shortcuts import render


class AlunoForm(forms.ModelForm):
    dataDeNasc = forms.DateField(
        label='Data de Nasccccccimento',
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
    ANO_CHOICES = [(str(i), str(i)) for i in range(1900, 2101)]  # Lista de anos de 1900 a 2100
    semestre = forms.ChoiceField(label="Semestre:", choices=[('', '---'),('1', '1'), ('2', '2')], required=False)
    # curso = forms.ModelChoiceField(label="Curso: ", queryset=Curso.objects.all(), required=False)
    curso = forms.ChoiceField(label="Curso:", choices=[('', '-----------'), ('Ciência da Computação', 'Ciência da Computação'), ('Medicina', 'Medicina'), ('Pedagogia', 'Pedagogia'), ('Teatro', 'Teatro')], required=False)

    campus = forms.ModelChoiceField(label="Campus: ", queryset=Campus.objects.all(), required=False)
    ano = forms.CharField(label="Ano: ", max_length=4, min_length=4, widget=forms.TextInput(attrs={'maxlength': '4'}), required=False)
    classificacao = forms.ChoiceField(label="Classificação:", choices=[('', '---------'), ('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnólogo', 'Tecnólogo')], required=False)
    modalidade = forms.ChoiceField(label="Modalidade", choices=[('', '------'), ('Presencial', 'Presencial'), ('Ensino a distância', 'Ensino a distância')], required=False)




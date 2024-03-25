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

class editarAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        # fields = '__all__'
        exclude = ['id','matricula','foto', 'dataDeNasc', 'cpf', 'formaDeIngresso']


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
    curso = forms.ChoiceField(label="Curso:", choices=[('', '-----------'), ('Ciência da Computação', 'Ciência da Computação'), ('Medicina', 'Medicina'), ('Pedagogia', 'Pedagogia'), ('Teatro', 'Teatro')], required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    campus = forms.ModelChoiceField(label="Campus:", queryset=Campus.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    pesquisa = forms.CharField(label="Matrúcula:", max_length=50, widget=forms.TextInput(attrs={'maxlength': '50', 'class': 'form-control'}), required=False)



# class AlunoForm(forms.ModelForm):
#     class Meta:
#         model = Aluno
#         fields = ['nome', 'cpf', 'curso', 'dataDeNasc', 'foto', 'situacao', 'formaDeIngresso', 'sexo', 'raca']
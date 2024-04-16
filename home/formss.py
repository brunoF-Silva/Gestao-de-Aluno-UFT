# # forms.py
# from django import forms
# from .models import Aluno, Campus
# from datetime import datetime
# from django.shortcuts import render


# class AlunoForm(forms.ModelForm):
#     dataDeNasc = forms.DateField(
#         label='Data de Nascimento',
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         input_formats=['%Y-%m-%d']
#     )

#     class Meta:
#         model = Aluno
#         exclude = ['situacao', 'matricula']

# class EditarAlunoForm(forms.ModelForm):
#     class Meta:
#         model = Aluno
#         # fields = '__all__'
#         exclude = ['id','matricula','foto', 'dataDeNasc', 'cpf', 'formaDeIngresso']


# # class FiltroForm(forms.Form):
# #     your_name = forms.CharField(label="Your name", max_length=100)
# #     from django import forms

# #     def __init__(self, *args, **kwargs):
# #         super(FiltroForm, self).__init__(*args, **kwargs)
# #         # Obtém todos os cursos disponíveis e define as escolhas do campo select
# #         self.fields['classificacao']  = forms.ChoiceField(choices=self.get_classificacao())       
# #         self.fields['campos'] = forms.ChoiceField(choices=self.get_choices())
        

# #     def get_choices(self):
# #         cursos = Curso.objects.all()
# #         # Cria uma lista de tuplas com os valores 'id' e 'nome' dos cursos
# #         return [(curso.id_curso, curso.nome) for curso in cursos]
    
# #     def get_classificacao(self):
# #         cursos = Curso.objects.all()
# #         # Cria uma lista de tuplas com os valores 'id' e 'nome' dos cursos
# #         return [(curso.id_curso, curso.classificacao) for curso in cursos]
    

# class DesvincularForm(forms.Form):
#     situacao = forms.ChoiceField(label="Situação:", choices=[('Formado', 'Formado'), ('Jubilado', 'Jubilado'), ('Evadido', 'Evadido')], required=True, widget=forms.Select(attrs={'class': 'form-select'}))
#     campoOculto = forms.CharField(widget=forms.HiddenInput)


# class FiltroForm(forms.Form):
#     curso = forms.ChoiceField(label="Curso:", choices=[('', '-----------'), ('Ciência da Computação', 'Ciência da Computação'), ('Medicina', 'Medicina'), ('Pedagogia', 'Pedagogia'), ('Teatro', 'Teatro')], required=False, widget=forms.Select(attrs={'class': 'form-select'}))
#     campus = forms.ModelChoiceField(label="Campus:", queryset=Campus.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
#     pesquisa = forms.CharField(label="Matrícula:", max_length=50, widget=forms.TextInput(attrs={'maxlength': '50', 'class': 'form-control'}), required=False)

#     # Adicione este método para definir as opções pré-selecionadas
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         # Se você passar dados iniciais para o formulário, defina as opções pré-selecionadas
#         if 'initial' in kwargs:
#             initial = kwargs['initial']
#             self.fields['curso'].initial = initial.get('curso')
#             self.fields['campus'].initial = initial.get('campus')


# # class AlunoForm(forms.ModelForm):
# #     class Meta:
# #         model = Aluno
# #         fields = ['nome', 'cpf', 'curso', 'dataDeNasc', 'foto', 'situacao', 'formaDeIngresso', 'sexo', 'raca']
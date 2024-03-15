# forms.py
from django import forms
from .models import Aluno
from datetime import datetime

class AlunoForm(forms.ModelForm):
    data_de_nasc = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Aluno
        exclude = ['situacao', 'matricula']

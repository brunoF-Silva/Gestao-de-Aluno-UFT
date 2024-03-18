from django import forms
from models import Aluno, Curso

class filtroForms(forms.ModelForm):
  class Meta:
    model 
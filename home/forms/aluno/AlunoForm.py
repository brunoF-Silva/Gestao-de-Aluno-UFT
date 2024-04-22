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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control'})
        self.fields['curso'].widget.attrs.update({'class': 'form-select', 'class': 'form-control'})
        self.fields['dataDeNasc'].widget.attrs.update({'class': 'form-control'})
        self.fields['formaDeIngresso'].widget.attrs.update({'class': 'form-select', 'class': 'form-control'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-select', 'class': 'form-control'})
        self.fields['raca'].widget.attrs.update({'class': 'form-select form-control'})
        self.fields['foto'].widget.attrs.update({'class': 'form-control', })

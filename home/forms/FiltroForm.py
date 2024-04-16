from django import forms
from home.models import Campus

class FiltroForm(forms.Form):
    curso = forms.ChoiceField(label="Curso:", choices=[('', '-----------'), ('Ciência da Computação', 'Ciência da Computação'), ('Medicina', 'Medicina'), ('Pedagogia', 'Pedagogia'), ('Teatro', 'Teatro')], required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    campus = forms.ModelChoiceField(label="Campus:", queryset=Campus.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select'}))
    pesquisa = forms.CharField(label="Matrícula:", max_length=50, widget=forms.TextInput(attrs={'maxlength': '50', 'class': 'form-control'}), required=False)

    # Adicione este método para definir as opções pré-selecionadas
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Se você passar dados iniciais para o formulário, defina as opções pré-selecionadas
        if 'initial' in kwargs:
            initial = kwargs['initial']
            self.fields['curso'].initial = initial.get('curso')
            self.fields['campus'].initial = initial.get('campus')
from django import forms

class DesvincularForm(forms.Form):
    situacao = forms.ChoiceField(label="Situação:", choices=[('Formado', 'Formado'), ('Jubilado', 'Jubilado'), ('Evadido', 'Evadido')], required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    campoOculto = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['situacao'].widget.attrs.update({'class': 'form-control'})
        
from django import forms

class DesvincularForm(forms.Form):
    situacao = forms.ChoiceField(label="Situação:", choices=[('Formado', 'Formado'), ('Jubilado', 'Jubilado'), ('Evadido', 'Evadido')], required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    campoOculto = forms.CharField(widget=forms.HiddenInput)
from django import forms

class ComentarioForm(forms.Form):
    
    texto = forms.CharField(widget=forms.Textarea)

class BuscaForm(forms.Form):
    busca = forms.CharField(required=False)
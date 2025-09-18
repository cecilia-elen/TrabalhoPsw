from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ('nome', 'CNPJ', 'estado', 'cidade', 'bairro', 'logradouro', 'numero', 'detalhamento','ramo')

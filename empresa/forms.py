from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
<<<<<<< HEAD
        fields = ('nome', 'CNPJ', 'estado', 'cidade', 'bairro', 'logradouro', 'numero', 'detalhamento','ramo')
        #
=======
        fields = ('nome_loja', 'cnpj', 'estado', 'cidade', 'bairro', 'logradouro', 'numero', 'detalhamento','ramo')

    
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

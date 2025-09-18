from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nome', 'cat_pai')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Este trecho torna o campo 'categoria_pai' opcional no formulário


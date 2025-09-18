from django import forms
from .models import Catalogo

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        # 'categoria' entra aqui, pois o usuário precisa escolher.
        fields = ('thumbnail', 'título', 'descrição', 'categoria')

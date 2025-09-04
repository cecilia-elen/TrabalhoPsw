from django import forms
from .models import Catalogo
from empresa.models import Empresa

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        # 'categoria' entra aqui, pois o usuário precisa escolher.
        fields = ('thumbnail', 'título', 'descrição', 'categoria', 'empresa')

#lógica para que apareça os campos com as empresas do usuário e o bootstrap de categorias
    def __init__(self, *args, **kwargs):
#remove o user que a view passou para remover ele do formulário base do django
        user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)
        # Filtra o campo 'empresa' para mostrar apenas as do usuário.
        if user:
            self.fields['empresa'].queryset = Empresa.objects.filter(usuario=user)
         # Adiciona uma classe ao widget do campo 'categoria'
        # para que o JavaScript Select2 possa encontrá-lo e fazer a formatação que tá no bootstrap
        self.fields['categoria'].widget.attrs.update({'class': 'select2-field'})
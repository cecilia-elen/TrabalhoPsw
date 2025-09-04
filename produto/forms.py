from django import forms
from .models import Produto, Catalogo_Produto
from empresa.models import Empresa

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'unidade', 'preco', 'descricao', 'imagem', 'categoria', 'empresa')

        # Ele garante que o dropdown 'empresa' só mostre as empresas do usuário logado.
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            self.fields['empresa'].queryset = Empresa.objects.filter(usuario=user)

class Catalogo_ProdutoForm(forms.ModelForm):
    class Meta:
        model = Catalogo_Produto
        fields = ('produto', 'preco_promocional')

    def __init__(self, empresa, *args, **kwargs):
        #Este método especial customiza o formulário. Ele garante que o campo 'produto' só mostre os produtos do usuário que é dono do catálogo, evitando que uma loja adicione produtos de outra por engano.
        super().__init__(*args, **kwargs)
        if empresa:
            self.fields['produto'].queryset = Produto.objects.filter(empresa=empresa)   
    
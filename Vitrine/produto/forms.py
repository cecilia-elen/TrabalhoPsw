from django import forms
from .models import Produto, Catalogo_Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'unidade', 'preco', 'descricao', 'imagem', 'categoria')

class Catalogo_ProdutoForm(forms.ModelForm):
    class Meta:
        model = Catalogo_Produto
        fields = ('produto', 'preco_promocional')

    def __init__(self, empresa, *args, **kwargs):
        #Este método especial customiza o formulário. Ele garante que o campo 'produto' só mostre os produtos do usuário que é dono do catálogo, evitando que uma loja adicione produtos de outra por engano.
        super().__init__(*args, **kwargs)
        if empresa:
            self.fields['produto'].queryset = Produto.objects.filter(usuario=user)   
    
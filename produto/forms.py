from django import forms
from django.core.files.uploadedfile import UploadedFile #pra verificar o tipo do arquivo importado
from .models import Produto, Catalogo_Produto
from empresa.models import Empresa

class ProdutoForm(forms.ModelForm):
    IMG = forms.ImageField(label="Imagem do Produto", required=False, widget=forms.ClearableFileInput)
    class Meta:
        model = Produto
        fields = ('nome', 'unidade', 'preco', 'descricao', 'IMG', 'categoria', 'empresa')

  #Método para tratar imagens blob, é mais prático colocar aqui pq evita repetiçoes no views
    def save(self, commit=True):
        instance = super().save(commit=False)
        uploaded_image = self.cleaned_data.get('IMG')
        if isinstance(uploaded_image, UploadedFile):
            instance.IMG = uploaded_image.read()
        if commit:
            instance.save()
        return instance

        # Ele garante que o dropdown 'empresa' só mostre as empresas do usuário logado.
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            self.fields['empresa'].queryset = Empresa.objects.filter(responsavel=user)


class Catalogo_ProdutoForm(forms.ModelForm):
    class Meta:
        model = Catalogo_Produto
        fields = ('produto', 'preco')

    def __init__(self, empresa, *args, **kwargs):
        #Este método especial customiza o formulário. Ele garante que o campo 'produto' só mostre os produtos do usuário que é dono do catálogo, evitando que uma loja adicione produtos de outra por engano.
        super().__init__(*args, **kwargs)
        if empresa:
            self.fields['produto'].queryset = Produto.objects.filter(empresa=empresa)   
    #
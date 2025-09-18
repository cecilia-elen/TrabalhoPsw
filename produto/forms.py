from django import forms
<<<<<<< HEAD
from django.core.files.uploadedfile import UploadedFile #pra verificar o tipo do arquivo importado
=======
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
from .models import Produto, Catalogo_Produto
from empresa.models import Empresa

class ProdutoForm(forms.ModelForm):
<<<<<<< HEAD
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
=======
    class Meta:
        model = Produto
        fields = ('nome', 'unidade', 'preco', 'descricao', 'imagem', 'categoria', 'empresa')
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

        # Ele garante que o dropdown 'empresa' só mostre as empresas do usuário logado.
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
<<<<<<< HEAD
            self.fields['empresa'].queryset = Empresa.objects.filter(responsavel=user)

=======
            self.fields['empresa'].queryset = Empresa.objects.filter(usuario=user)
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

class Catalogo_ProdutoForm(forms.ModelForm):
    class Meta:
        model = Catalogo_Produto
<<<<<<< HEAD
        fields = ('produto', 'preco')
=======
        fields = ('produto', 'preco_promocional')
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

    def __init__(self, empresa, *args, **kwargs):
        #Este método especial customiza o formulário. Ele garante que o campo 'produto' só mostre os produtos do usuário que é dono do catálogo, evitando que uma loja adicione produtos de outra por engano.
        super().__init__(*args, **kwargs)
        if empresa:
            self.fields['produto'].queryset = Produto.objects.filter(empresa=empresa)   
<<<<<<< HEAD
    #
=======
    
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

from django import forms
from .models import Catalogo
from django.core.files.uploadedfile import UploadedFile #pra verificar o tipo do arquivo importado
from empresa.models import Empresa

class CatalogoForm(forms.ModelForm):
    IMG = forms.ImageField(label="Imagem do Catálogo", required=False, widget=forms.ClearableFileInput)
    class Meta:
        model = Catalogo
        # 'categoria' entra aqui, pois o usuário precisa escolher.
        fields = ('IMG', 'nome', 'descricao', 'categoria', 'empresa')

#Método para tratar imagens blob, é mais prático colocar aqui pq evita repetiçoes no views
    def save(self, commit=True):
        instance = super().save(commit=False)
        uploaded_image = self.cleaned_data.get('IMG')
        if isinstance(uploaded_image, UploadedFile):
            instance.IMG = uploaded_image.read()
        if commit:
            instance.save()
        return instance

#lógica para que apareça os campos com as empresas do usuário e o bootstrap de categorias
    def __init__(self, *args, **kwargs):
#remove o user que a view passou para remover ele do formulário base do django
        user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)
        # Filtra o campo 'empresa' para mostrar apenas as do usuário.
        if user:
            self.fields['empresa'].queryset = Empresa.objects.filter(responsavel=user)
         # Adiciona uma classe ao widget do campo 'categoria'
        # para que o JavaScript Select2 possa encontrá-lo e fazer a formatação que tá no bootstrap
        self.fields['categoria'].widget.attrs.update({'class': 'select2-field'})
        #
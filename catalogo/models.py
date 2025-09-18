from django.db import models
from empresa.models import Empresa
from categoria.models import Categoria
from Vitrine.mixins import ImageHandlerMixin



class Catalogo(ImageHandlerMixin, models.Model):
    # muitos catálogos podem pertencer a uma empresa n:1 .
    # Se a empresa for deletada, todos os seus catálogos também serão.
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="catalogos", null=True, blank=True)
    # Se a categoria for deletada, o catálogo não será, ele apenas ficará "sem categoria", o que é mais seguro.
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="catalogos")
    nome = models.CharField(max_length=60, help_text="Ex: Coleção Verão 2025, Mercearia, Roupas, Sobremesas...")
    descricao = models.CharField(max_length=80, blank=True, null=True, help_text="Diga brevemente o que o catálogo aborda (se necessário)")
    #Arquivo em BLOB (no django ele fica BinaryField, porque blob é Binary Large Object, assim, o arquivo passa a armazenar os dados brutos da imagem diretamente no banco de dados, em vez de salvar o arquivo em uma pasta e apenas guardar o caminho até ele)
    IMG = models.BinaryField(blank=True, null=True, verbose_name="Imagem Binária", editable=True)
    
    def __str__(self):
        return f"{self.nome} ({self.empresa.nome})"

    class Meta:
        # Garante que não exista outro catálogo com o mesmo título para a mesma empresa
        unique_together = ('empresa', 'nome')
        verbose_name_plural = "Catálogos"
        #
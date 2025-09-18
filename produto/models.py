from django.db import models
from empresa.models import Empresa
from catalogo.models import Catalogo
from categoria.models import Categoria
from Vitrine.mixins import ImageHandlerMixin
from django.conf import settings # Importa as configurações

class Produto(ImageHandlerMixin, models.Model):
    # Cada produto pertence a uma única empresa n:1
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="produtos", null=True, blank=True)
    nome = models.CharField(max_length=200)
    unidade = models.CharField(max_length=50, help_text="Unidade de venda do produto (ex: Peça, Kg, Caixa com 12, Pacote 500g)")
    # Categoria para filtrar produtos por ela.
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="produtos")
    # DecimalField para evitar problemas de arredondamento
    preco = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço do produto")
    descricao = models.TextField(verbose_name="Descrição")
    #Arquivo em BLOB (no django ele fica BinaryField, porque blob é Binary Large Object, assim, o arquivo passa a armazenar os dados brutos da imagem diretamente no banco de dados, em vez de salvar o arquivo em uma pasta e apenas guardar o caminho até ele)
    IMG = models.BinaryField(blank=True, null=True, verbose_name="Imagem Binária", editable=True)
    # A "ponte" para os catálogos.(um produto pode estar em muitos Catálogos, através do modelo 'Catalogo_Produto')
    catalogos = models.ManyToManyField(Catalogo, through='Catalogo_Produto', related_name='produtos')

    def __str__(self):
        return self.nome


#o models de Catalogo_produto, que liga a informação de ambas as classes para otimizar a escolha de produtos para catálogos diferentes, preços promocionais... etc
class Catalogo_Produto(models.Model):
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,help_text="Use se o preço neste catálogo for diferente do padrão.")


# transforma um método em atributo Verifica se um preço promocional foi definido para este produto especificamente neste catálogo.Se um 'preco_promocional' existir, ele tem prioridade e é retornado, se 'preco_promocional' for nulo (vazio), o sistema busca e retorna o preço do modelo original do Produto.
    @property
    def preco_final(self):
        return self.preco if self.preco is not None else self.produto.preco

    class Meta:
        unique_together = ('catalogo', 'produto')
#tal produto em tal catálogo
    def __str__(self):
        return f"{self.produto.nome} em {self.catalogo.nome}"
    #
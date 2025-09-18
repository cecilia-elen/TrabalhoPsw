from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator #valor mínimo e máximo de inteiros para o número das casas
from Vitrine.mixins import ImageHandlerMixin
    
class Usuario(User, ImageHandlerMixin):

    cpf = models.CharField(max_length=14,unique=True,verbose_name='CPF',help_text='Informe o CPF no formato 000.000.000-00')
     #Arquivo em BLOB (no django ele fica BinaryField, porque blob é Binary Large Object, assim, o arquivo passa a armazenar os dados brutos da imagem diretamente no banco de dados, em vez de salvar o arquivo em uma pasta e apenas guardar o caminho até ele)
    foto_perfil = models.BinaryField(blank=True, null=True, verbose_name="Imagem Binária", editable=True)
    sobre = models.TextField(verbose_name='Sobre', blank=True, null=True, help_text='Coloque aqui informações sobre você, slogan, um texto atrativo... como quiser!')
    estado = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)], blank=True, null=True)
    detalhamento = models.CharField(max_length=100, blank=True, null=True)
    Telefone = models.CharField(max_length=15, null=True, blank=True)

    # Redes Sociais (usando URLField para garantir que seja um link válido)
    X = models.URLField(max_length=200, null=True, blank=True, verbose_name="X (Twitter)")
    Facebook = models.URLField(max_length=200, null=True, blank=True)
    Instagram = models.URLField(max_length=200, null=True, blank=True)
    Youtube = models.URLField(max_length=200, null=True, blank=True)
    Github = models.URLField(max_length=200, null=True, blank=True)
    LinkedIn = models.URLField(max_length=200, null=True, blank=True)
    Kwai = models.URLField(max_length=200, null=True, blank=True)
    Tiktok = models.URLField(max_length=200, null=True, blank=True)
    Telegram = models.URLField(max_length=200, null=True, blank=True)
    Whatsapp = models.URLField(max_length=200, null=True, blank=True)
    image_field_name = 'foto_perfil'

    @property
    def perfil_completo(self):

    #Retorna True se os campos essenciais do perfil estiverem preenchidos.
        campos_obrigatorios = [self.sobre,self.estado,self.cidade,self.bairro,self.logradouro,self.numero]
        return all(campos_obrigatorios)
    

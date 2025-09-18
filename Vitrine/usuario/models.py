from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator #valor mínimo e máximo de inteiros para o número das casas
from django.db.models.signals import post_save

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
     # Diz ao Django que o campo de login agora é o 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    cpf = models.CharField(max_length=14,unique=True,verbose_name='CPF',help_text='Informe o CPF no formato 000.000.000-00')
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    sobre = models.TextField(verbose_name='Sobre', blank=True, null=True, help_text='Coloque aqui informações sobre seu comércio, slogan, um texto atrativo... como quiser!')
    estado = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
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



    def __str__(self):
        return self.email # Isso ajuda a ver o email do usuário no painel admin

    class Meta:
        permissions = [
            ('detalha_pessoa', 'Pode ver detalhes de uma pessoa em específico')
        ]
    def get_display_name(self):
        """
        Retorna o nome de exibição do usuário, com uma ordem de prioridade:
        1. Nome da Loja (se existir), lá no app de empresa
        2. Nome Completo 
        """
        # hasattr verifica se o perfil já foi criado para evitar erros
        if hasattr(self, 'empresa') and self.empresa.nome_loja:
            return self.empresa.nome_loja
        
        else:
            return f"{self.first_name} {self.last_name}"
        
    @property
    def perfil_completo(self):

    #Retorna True se os campos essenciais do perfil estiverem preenchidos.
        campos_obrigatorios = [self.sobre,self.estado,self.cidade,self.bairro,self.endereco,self.numero]
        return all(campos_obrigatorios)
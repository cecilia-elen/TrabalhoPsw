from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager #É pra que o super user funcione direito, porque o email vira o username na minha costumizaçao de user do django 
from django.core.validators import MinValueValidator, MaxValueValidator #valor mínimo e máximo de inteiros para o número das casas
from django.db.models.signals import post_save

class UserManager(BaseUserManager):

    #Manager customizado para o modelo Usuario onde o email é o identificador únicoem vez do username.

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O Email é um campo obrigatório')
        email = self.normalize_email(email)
        # Define o username para ser igual ao email, garantindo que o campo não fique vazio
        username = email
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O superuser deve ter is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
    
class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
     # Diz ao Django que o campo de login agora é o 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()
    cpf = models.CharField(max_length=14,unique=True,verbose_name='CPF',help_text='Informe o CPF no formato 000.000.000-00')
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
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



    def __str__(self):
        return self.email # Isso ajuda a ver o email do usuário no painel admin

    class Meta:
        permissions = [
            ('detalha_pessoa', 'Pode ver detalhes de uma pessoa em específico')
        ]
        
    @property
    def perfil_completo(self):

    #Retorna True se os campos essenciais do perfil estiverem preenchidos.
        campos_obrigatorios = [self.sobre,self.estado,self.cidade,self.bairro,self.logradouro,self.numero]
        return all(campos_obrigatorios)
    

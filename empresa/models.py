from django.db import models
from django.contrib.auth import get_user_model

class Empresa(models.Model):
<<<<<<< HEAD
    nome = models.CharField(max_length=255, verbose_name="Nome da Loja/Empresa")
    CNPJ = models.CharField(max_length=18, unique=True, null=True, blank=True, verbose_name="CNPJ")
=======
    nome_loja = models.CharField(max_length=255, verbose_name="Nome da Loja/Empresa")
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True, verbose_name="CNPJ")
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08
    ramo = models.CharField(max_length=100, verbose_name="Ramo de Atividade")
    # Endereço da Empresa
    estado = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    logradouro = models.CharField(max_length=255, null=True, blank=True, verbose_name="Endereço")
    numero = models.CharField(max_length=10, null=True, blank=True, verbose_name="Número")
    detalhamento = models.CharField(max_length=255, null=True, blank=True, verbose_name="Complemento", help_text="Ex: Sala 10, Bloco C")

    # A relação 1:n com o usuário
<<<<<<< HEAD
    responsavel = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='empresas')
=======
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='empresas')
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08



 # Se o usuário tiver colocado um endereço próprio para a empresa, ele vai aparecer, senão, vai aparecer o que ela colocou no perfil
    @property
    def cidade_display(self):
<<<<<<< HEAD
        return self.cidade if self.cidade else self.responsavel.cidade

    @property
    def estado_display(self):
        return self.estado if self.estado else self.responsavel.estado
    @property
    def bairro_display(self):
        return self.bairro if self.bairro else self.responsavel.bairro
    
    @property
    def logradouro_display(self):
        return self.logradouro if self.logradouro else self.responsavel.logradouro
    @property
    def numero_display(self):
        return self.numero if self.numero else self.responsavel.numero
    @property
    def detalhamento_display(self):
        return self.detalhamento if self.detalhamento else self.responsavel.detalhamento
    def __str__(self):
        return self.nome
    #
=======
        return self.cidade if self.cidade else self.usuario.cidade

    @property
    def estado_display(self):
        return self.estado if self.estado else self.usuario.estado
    @property
    def bairro_display(self):
        return self.bairro if self.bairro else self.usuario.bairro
    
    @property
    def logradouro_display(self):
        return self.logradouro if self.logradouro else self.usuario.logradouro
    @property
    def numero_display(self):
        return self.numero if self.numero else self.usuario.numero
    @property
    def detalhamento_display(self):
        return self.detalhamento if self.detalhamento else self.usuario.detalhamento
    def __str__(self):
        return self.nome_loja
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

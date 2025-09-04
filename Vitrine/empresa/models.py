from django.db import models
from django.contrib.auth import get_user_model

class Empresa(models.Model):
    nome_loja = models.CharField(max_length=255, verbose_name="Nome da Loja/Empresa")
    cnpj = models.CharField(max_length=18, unique=True, null=True, blank=True, verbose_name="CNPJ")
    ramo = models.CharField(max_length=100, null=True, blank=True, verbose_name="Ramo de Atividade")
    # Endereço da Empresa
    estado = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True, verbose_name="Endereço")
    numero = models.CharField(max_length=10, null=True, blank=True, verbose_name="Número")
    detalhamento = models.CharField(max_length=255, null=True, blank=True, verbose_name="Complemento", help_text="Ex: Sala 10, Bloco C")

    # A relação 1:1 com o usuário
    usuario = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_loja
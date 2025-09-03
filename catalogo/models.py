from django.db import models
<<<<<<< HEAD
from empresa.models import Empresa
from categoria.models import Categoria


class Catalogo(models.Model):
    # muitos catálogos podem pertencer a uma empresa n:1 .
    # Se a empresa for deletada, todos os seus catálogos também serão.
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="catalogos", null=True, blank=True)
    # Se a categoria for deletada, o catálogo não será, ele apenas ficará "sem categoria", o que é mais seguro.
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="catalogos")
    título = models.CharField(max_length=60, help_text="Ex: Coleção Verão 2025, Mercearia, Roupas, Sobremesas...")
    descrição = models.CharField(max_length=80, blank=True, null=True, help_text="Diga brevemente o que o catálogo aborda (se necessário)")
    thumbnail = models.ImageField(upload_to='thumbnails_catalogos/', blank=True, null=True, help_text="Uma imagem de capa para o catálogo")
    # Um campo extra útil para ativar/desativar o catálogo sem precisar apagar
    esta_ativo = models.BooleanField(default=True, verbose_name="Está ativo?")

    def __str__(self):
        return f"{self.título} ({self.empresa.nome_loja})"

    class Meta:
        # Garante que não exista outro catálogo com o mesmo título para a mesma empresa
        unique_together = ('empresa', 'título')
        verbose_name_plural = "Catálogos"
=======

# Create your models here.
>>>>>>> 1cea6da5e9c6ae1a5fcfbe83fecbbd074ab1453d

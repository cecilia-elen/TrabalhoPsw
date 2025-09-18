from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, help_text="Nome da categoria (ex: Roupas, Vestidos)")
    # ForeignKey para 'self' (o próprio modelo Categoria) para que a gente possa criar categorias filha de uma certa categoria
<<<<<<< HEAD
    cat_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategorias',verbose_name="Categoria Principal")

    def __str__(self):
    #Mostra o caminho completo da categoria, por exemplo: Roupas > Vestidos
        if self.cat_pai:
            return f'{self.cat_pai} > {self.nome}'
        return self.nome

    class Meta:
        verbose_name_plural = "Categorias"
        #
=======
    categoria_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategorias',verbose_name="Categoria Principal")

    def __str__(self):
    #Mostra o caminho completo da categoria, por exemplo: Roupas > Vestidos
        if self.categoria_pai:
            return f'{self.categoria_pai} > {self.nome}'
        return self.nome

    class Meta:
        verbose_name_plural = "Categorias"
>>>>>>> 8750437900de8beadd7384be3adc93d797d65d08

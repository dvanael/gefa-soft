from django.db import models

# Create your models here.
class Produto(models.Model):
    UNIDADE_CHOICES = [
        ('Kg', 'Kg'),
        ('Un', 'Un'),
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome')
    unidade = models.CharField(max_length=100, verbose_name='Unidade', choices=UNIDADE_CHOICES)
    preco = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preco')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f"{self.nome} - R${self.preco} ({self.unidade})"

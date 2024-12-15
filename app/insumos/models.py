from django.db import models

class Insumo(models.Model):
    tipo = models.CharField(max_length=45, verbose_name='Tipo do Insumo')
    preco = models.DecimalField(verbose_name='Preço Unitário', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

    def __str__(self):
        return f"{self.tipo} - R${self.preco}"

from django.db import models

class TipoInsumo(models.Model):
    tipo = models.CharField(verbose_name='Tipo', max_length=45)
    
    def __str__(self):
        return self.tipo

class Insumo(models.Model):
    tipo = models.ForeignKey(TipoInsumo, on_delete=models.PROTECT, verbose_name='Tipo do insumo')
    preco = models.DecimalField(verbose_name='Preço unitário', max_digits=5, decimal_places=2)
    
    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'
    
    def __str__(self):
        return f"{self.tipo}"

    
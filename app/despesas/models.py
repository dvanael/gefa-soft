from django.db import models
from app.insumos.models import Insumo
# Create your models here.
class GastoInsumo(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT, verbose_name='Insumo')
    quantidade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Quantidade')

    def __str__(self):
        return f'{self.insumo} - Qntd. {self.quantidade} - Total: R${self.total}'

    @property
    def total(self):
        return self.quantidade * self.insumo.preco
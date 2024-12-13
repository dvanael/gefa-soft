from django.db import models
from app.insumos.models import Insumo
from app.funcionarios.models import Producao
# Create your models here.
class GastoInsumo(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT, verbose_name='Insumo')
    quantidade = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Quantidade')

    class Meta:
        verbose_name = 'Gasto de Insumo'
        verbose_name_plural = 'Gastos de Insumos'

    def __str__(self):
        return f'{self.insumo} - Qntd. {self.quantidade} - Total: R${self.total}'

    @property
    def total(self):
        return self.quantidade * self.insumo.preco


class PagamentoFuncionario(models.Model):
    funcionario = models.ForeignKey('funcionarios.Funcionario', on_delete=models.PROTECT, verbose_name='Funcionario')
    data_pagemento = models.DateField(verbose_name='Data')
    data = models.DateField(verbose_name='Data', auto_now_add=True)

    class Meta:
        verbose_name = 'Pagamento de Funcionário'
        verbose_name_plural = 'Pagamentos de Funcionários'

    def __str__(self):
        return f'{self.funcionario} - {self.data}'

    @property
    def valor_mensal(self, mes: models.DateField):
        producoes = Producao.objects.filter(funcionario=self.funcionario, data__month=mes)
        valor_mensal = 0
        for producao in producoes:
            valor_mensal += self.funcionario.preco_trabalho * producao.quantidade

        return valor_mensal
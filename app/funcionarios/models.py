from django.db import models
from app.produtos.models import Produto


class Funcionario(models.Model):
    FUNCAO_CHOICES = [
        ("Gomeiro(a)", "Gomeiro(a)"),
        ("Forneiro(a)", "Forneiro(a)"),
        ("Raspadeiro(a)", "Raspadeiro(a)"),
    ]
    nome = models.CharField(verbose_name="Nome", max_length=60, null=False)
    funcao = models.CharField(
        verbose_name="Função", max_length=60, null=False, choices=FUNCAO_CHOICES
    )
    preco_trabalho = models.DecimalField(
        verbose_name="Preço do Trabalho",
        max_digits=5,
        decimal_places=2,
        null=False,
        default=0.00,
    )

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return f"{self.nome} - {self.funcao}"


class Producao(models.Model):
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.PROTECT, verbose_name="Funcionário"
    )
    produto = models.ForeignKey(
        Produto, on_delete=models.PROTECT, verbose_name="Produto"
    )
    quantidade = models.DecimalField(
        verbose_name="Quantidade", max_digits=5, decimal_places=2, null=False
    )
    data = models.DateField(verbose_name="Dia da Produção", null=False)

    class Meta:
        verbose_name = "Produção"
        verbose_name_plural = "Produções"
        ordering = ["-data"]

    def __str__(self):
        return f"{self.funcionario} - {self.produto.nome} - {self.quantidade} {self.produto.unidade}"

    @property
    def saldo(self):
        return self.quantidade * self.produto.preco

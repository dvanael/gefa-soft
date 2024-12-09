from django.db import models

class Funcionario(models.Model):
    FUNCAO_CHOICES = [
        ('Gomeiro(a)', 'Gomeiro(a)'),
        ('Forneiro(a)', 'Forneiro(a)'),
        ('Raspadeiro(a)', 'Raspadeiro(a)'),
    ]
    nome = models.CharField(verbose_name="Nome", max_length=60, null=False)
    funcao = models.CharField(verbose_name="Função", max_length=60, null=False, choices=FUNCAO_CHOICES)
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
    
    def __str__(self):
        return f"{self.nome} - {self.funcao}"

from django.db import models
from materiaPrima.models import MateriaPrima
# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    materias_primas = models.ManyToManyField(MateriaPrima, through='ProdutoMateriaPrima')

    def __str__(self):
        return self.nome

class ProdutoMateriaPrima(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.produto} - {self.materia_prima.nome}: {self.quantidade}'

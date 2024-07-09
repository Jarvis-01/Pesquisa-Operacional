from django.db import models

class MateriaPrima(models.Model):
    nome = models.CharField(max_length=100)
    disponivel = models.IntegerField(null=True)
    preco = models.FloatField(null=True)

    def __str__(self):
        return self.nome

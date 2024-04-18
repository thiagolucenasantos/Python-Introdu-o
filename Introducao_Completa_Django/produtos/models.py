from django.db import models

# Create your models here.
class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco = models.FloatField()

    def __str__(self) -> str:
        return self.nome_produto
from django.db import models
from myauth.models import *
from produto.models import *


class ProdutoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(verbose_name="Quantidade de produto:")
  
    class Meta:
        verbose_name = "Estoque"
        verbose_name_plural = "Estoques"
        db_table = "Estoque"

    def __str__(self):
        return self.produto.nome

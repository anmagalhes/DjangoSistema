from django.db import models

from django.contrib.auth.models import User


class Pedido(models.Model):
    STATUSPEDIDO_CHOICES = (
        ('A', 'Aprovado'),
        ('C', 'Criado'),
        ('E', 'Enviado'),
        ('F', 'Finalizado'),
        ('R', 'Reprovado'),
        ('p', 'Pendente'),
    )
    # usuario =models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    statuspedido = models.CharField(
        default='C',
        max_length=1,
        choices=STATUSPEDIDO_CHOICES,
        null=False,
    )


def __str__(self) -> str:
    return f'Pedido N. {self.pk}'


class Itempedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    codproduto = models.PositiveIntegerField()
    nomeproduto = models.CharField(max_length=255)
    preco_produto = models.FloatField()
    quantidade_Material = models.PositiveIntegerField()
    imagem = models.CharField(max_length=2000)


def __str__(self) -> str:
    return f'item do {self.pedido}'


class Meta:
    verbose_name = 'item do pedidos'
    verbose_name_plural = 'itens dos pedidos'

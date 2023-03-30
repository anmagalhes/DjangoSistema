from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(
        'Nome Categoria', help_text='Nome Completo Catergoria', max_length=40
    )

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.Categoria.titulo


class Produto(models.Model):
    nome = models.CharField(
        'Nome do Produto',
        help_text='Nome Completo Produto',
        max_length=255,
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null='true'
    )
    quantidade = models.FloatField(
        'Quantidade do produto',
        help_text='Quantidade produto, Sem traços ou pontos',
        default=0,
    )

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.produto.nome


class ProdutoEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField('Quantidade de produto:')

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'
        db_table = 'Estoque'

    def __str__(self):
        return self.produto.nome

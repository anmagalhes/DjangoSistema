from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(
        'Nome Categoria', 
        help_text='Nome Completo Catergoria',    
          max_length=40
          )

def __str__(self):
    return self.Categoria.titulo

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "Categoria"

class Produto(models.Model):
    nome = models.CharField(
         'Nome do Produto', 
         help_text='Nome Completo Produto',  
         max_length=255,
         )
    categoria = models.ForeignKey(
        Categoria,  
        on_delete=models.SET_NULL, null='true'

    )
    quantidade = models.FloatField(
        'Quantidade do produto',
        help_text='Quantidade produto, Sem traços ou pontos',  
        default=0,
    )


class Meta:
        verbose_name = "produto"
        verbose_name_plural = "Produtos"
        db_table = "Produto"


def __str__(self):
    return self.produto.nome


# def gerar_desconto(self, desconto):
#   return self.quantidade -((self.quantidade * desconto ) /100)

# def lucro(self):
#  lucro = self.preco_venda - self.preco_compra
#  return (lucro * 100) / self.preco_compra

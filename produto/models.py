from django.db import models

class Categoria(models.Model):
 titulo = models.CharField(max_length=40)

def __str__(self) -> str:
 return self.titulo



class Produto(models.Model):
    nome = models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null="true")
    quantidade = models.FloatField(
    default=0,
    )

def __str__(self) -> str:
    return self.nome

 #def gerar_desconto(self, desconto):
#   return self.quantidade -((self.quantidade * desconto ) /100)

#def lucro(self):
 #  lucro = self.preco_venda - self.preco_compra
 #  return (lucro * 100) / self.preco_compra

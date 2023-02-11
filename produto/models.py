from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.titulo


class Produto(models.Model):

    nome = models.CharField(max_length=80)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null="true")
    quantidade = models.FloatField()
    

    def __str__(self) -> str:
        return self.Produto
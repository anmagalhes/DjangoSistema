from django.db import models


class Departamento(models.Model):
    nome = models.CharField(
        'Nome do Departamento',
        help_text='Nome Completo do Departanento',
        max_length=80,
    )


def __str__(self):
    return self.Departamento.nome


class Meta:
    verbose_name = 'departamento'
    verbose_name_plural = 'departamentos'

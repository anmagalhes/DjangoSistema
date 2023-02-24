from django.db import models
from funcionario.models import Funcionario


class Documentosrh(models.Model):
    descricao = models.CharField(
        'Nome do documento',
        help_text='Nome do documento completo',
        max_length=100
    )
    #pertence = models.ForeignKey(
     #   Funcionario,
      #  on_delete=models.SET_NULL,
      #  null=True,
      #  blank=True,
      #  help_text='Nome do documento completo',
   # )

    def __str__(self):
        return self.Documentosrh.descricao


class Meta:
    verbose_name = 'departamento'
    verbose_name_plural = 'departamentos'

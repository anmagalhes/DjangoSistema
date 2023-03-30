from django.db import models
from django.urls import reverse_lazy


class Departamento(models.Model):
    nome = models.CharField(
        'Nome do Departamento',
        help_text='Nome Completo do Departanento',
        max_length=80,
    )

    class Meta:
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'

    def __str__(self):
        return self.nome

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('departamento:departamento_update', kwargs=kw)
        return None

from django.db import models
from django.urls import reverse_lazy

from .constants import ESTADO_CHOICES, LOGRADOURO_CHOICES


class Endereco(models.Model):
    logradouro = models.CharField(
        'Logradouro',
        help_text='Nome do Logradouro',
        max_length=9,
        choices=LOGRADOURO_CHOICES,
        null=False,
        blank=False,
        default='Rua',
    )

    nome_do_logradouro = models.CharField(
        'Nome do Logradouro',
        help_text='Nome do Logradouro',
        max_length=70,
        null=False,
        blank=False,
    )

    numero = models.CharField(
        'Numero',
        help_text='Numero da Residencia',
        max_length=7,
        null=False,
        blank=False,
    )

    complemento = models.CharField(
        'Complemento',
        help_text='Complemento Casa ou Apptamento',
        max_length=7,
        null=False,
        blank=False,
    )

    bairro = models.CharField(
        'Bairro',
        help_text='Bairro da Residencia',
        max_length=70,
        null=False,
        blank=False,
    )

    cidade = models.CharField(
        'Cidade',
        help_text='Cidade da Residencia',
        max_length=70,
        null=False,
        blank=False,
    )

    estado = models.CharField(
        'Estado',
        help_text='Nome do Estado',
        max_length=9,
        choices=ESTADO_CHOICES,
        null=False,
        blank=False,
        default='CE',
    )

    cep = models.CharField(
        'Cep',
        help_text='Cep da Residencia',
        max_length=9,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.logradouro

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('endereco:endereco_update', kwargs=kw)
        return None

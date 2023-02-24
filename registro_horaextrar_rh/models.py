from django.db import models
from funcionario.models import Funcionario


# Create your models here.
class HoraExtra_Funcionario(models.Model):
    motivo = models.CharField(
        'Motivo Hora Extra',
        help_text='Nome do Motivo Hora extrar',
        max_length=100,
        null=False,
        blank=False,
    )
    Logradouro = models.CharField(
        'Logradouro',
        help_text='Nome do Logradouro',
        max_length=9,
        null=False,
        blank=False,
        default='Rua',
    )
from django.db import models


# Create your models here.
class HoraExtra_Funcionario(models.Model):
    Logradouro = models.CharField(
        'Logradouro',
        help_text='Nome do Logradouro',
        max_length=9,
        null=False,
        blank=False,
        default='Rua',
    )
from django.db import models


LOGRADOURO_CHOICES = [
    ('Rua', 'Rua'),
    ('Avenida', 'Avenida'),
    ('Praca', 'Praca'),
    ('Estrada', 'Estrada'),
    ('Travessa', 'Travessa'),
    ('Viela', 'Viela'),
    ('Passagem', 'Passagem'),
]

ESTADO_CHOICES = [
    ('AC', 'AC'),
    ('AP', 'AM'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]

# Create your models here.
class Endereco(models.Model):
    Logradouro = models.CharField(
        'Logradouro',
        help_text='Nome do Logradouro',
        max_length=9,
        choices=LOGRADOURO_CHOICES,
        null=False,
        blank=False,
        default='Rua',
    )

    Nome_do_Logradouro = models.CharField(
        'Nome do Logradouro',
        help_text='Nome do Logradouro',
        max_length=70,
        null=False,
        blank=False,
    )

    Numero = models.CharField(
        'Numero',
        help_text='Numero da Residencia',
        max_length=7,
        null=False,
        blank=False,
    )

    Complem = models.CharField(
        'Complemento',
        help_text='Complemento Casa ou Apptamento',
        max_length=7,
        null=False,
        blank=False,
    )

    Bairro = models.CharField(
        'Bairro',
        help_text='Bairro da Residencia',
        max_length=70,
        null=False,
        blank=False,
    )

    Cidade = models.CharField(
        'Cidade',
        help_text='Cidade da Residencia',
        max_length=70,
        null=False,
        blank=False,
    )

    Estado = models.CharField(
        'Estado',
        help_text='Nome do Estado',
        max_length=9,
        choices=ESTADO_CHOICES,
        null=False,
        blank=False,
        default='CE',
    )

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

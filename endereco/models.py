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
        (u'AC', u'AC'),
        (u'AP', u'AM'),
        (u'AM', u'AM'),
        (u'BA', u'BA'),
        (u'CE', u'CE'),
        (u'DF', u'DF'),
        (u'ES', u'ES'),
        (u'GO', u'GO'),
        (u'MA', u'MA'),
        (u'MT', u'MT'),
        (u'MS', u'MS'),
        (u'MG', u'MG'),
        (u'PA', u'PA'),
        (u'PB', u'PB'),
        (u'PR', u'PR'),
        (u'PE', u'PE'),
        (u'PI', u'PI'),
        (u'RJ', u'RJ'),
        (u'RN', u'RN'),
        (u'RS', u'RS'),
        (u'RO', u'RO'),
        (u'RR', u'RR'),
        (u'SC', u'SC'),
        (u'SP', u'SP'),
        (u'SE', u'SE'),
        (u'TO', u'TO'),
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
        choices= ESTADO_CHOICES,
        null=False,
        blank=False,
        default='Rua',
    )
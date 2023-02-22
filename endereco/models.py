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

# Create your models here.
class Endereco(models.Model):
    Logradouro =  models.CharField(
          'Logradouro',
        help_text='teste',
        max_length=9,
        choices= LOGRADOURO_CHOICES,
        null=False,
        blank=False,
        default='Rua'
    )

   
# Generated by Django 4.1.6 on 2023-02-22 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='Logradouro',
            field=models.CharField(
                choices=[
                    ('Rua', 'Rua'),
                    ('Avenida', 'Avenida'),
                    ('Praca', 'Praca'),
                    ('Estrada', 'Estrada'),
                    ('Travessa', 'Travessa'),
                    ('Viela', 'Viela'),
                    ('Passagem', 'Passagem'),
                ],
                default='Rua',
                help_text='teste',
                max_length=9,
                verbose_name='Logradouro',
            ),
        ),
    ]

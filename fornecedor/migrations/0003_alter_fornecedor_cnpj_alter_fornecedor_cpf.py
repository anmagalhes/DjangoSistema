# Generated by Django 4.1.6 on 2023-02-22 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'fornecedor',
            '0002_remove_fornecedor_profissao_remove_fornecedor_sexo_and_more',
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='CNPJ',
            field=models.CharField(
                blank=True,
                help_text='Número do CNPJ, Sem traços ou pontos',
                max_length=20,
                verbose_name='Número do CNPJ',
            ),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='CPF',
            field=models.CharField(
                blank=True,
                help_text='Número do CPF, Sem traços ou pontos',
                max_length=15,
                verbose_name='Número do CPF',
            ),
        ),
    ]

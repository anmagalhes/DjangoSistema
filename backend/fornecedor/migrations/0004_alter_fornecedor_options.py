# Generated by Django 4.1.7 on 2023-03-30 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0003_alter_fornecedor_cnpj_alter_fornecedor_cpf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
    ]

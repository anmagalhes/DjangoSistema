# Generated by Django 4.1.6 on 2023-02-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='profissao',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='sexo',
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='CNPJ',
            field=models.CharField(
                default='',
                help_text='Número do CNPJ, Sem traços ou pontos',
                max_length=20,
                verbose_name='Número do CNPJ',
            ),
            preserve_default=False,
        ),
    ]

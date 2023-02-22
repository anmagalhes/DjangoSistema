# Generated by Django 4.1.6 on 2023-02-22 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'nome',
                    models.CharField(
                        help_text='Nome Completo do Fornecedor',
                        max_length=80,
                        verbose_name='Nome do Fornecedor',
                    ),
                ),
                (
                    'CPF',
                    models.CharField(
                        help_text='Número do CPF, Sem traços ou pontos',
                        max_length=15,
                        verbose_name='Número do CPF',
                    ),
                ),
                (
                    'rg',
                    models.CharField(
                        help_text='RG Sem traços ou pontos',
                        max_length=15,
                        verbose_name='RG',
                    ),
                ),
                (
                    'datanascimento',
                    models.DateField(
                        blank=True,
                        help_text='Data de Nascimento do Fornecedor',
                        null=True,
                        verbose_name='Data de nascimento',
                    ),
                ),
                (
                    'sexo',
                    models.CharField(
                        choices=[
                            ('M', 'Masculino'),
                            ('F', 'Feminino'),
                            ('O', 'Outros'),
                        ],
                        default='M',
                        help_text='Escolha umas das opções',
                        max_length=1,
                        verbose_name='Sexo',
                    ),
                ),
                (
                    'profissao',
                    models.CharField(
                        blank=True,
                        help_text='Profissão Auto Declarada do Fornecedor',
                        max_length=80,
                        null=True,
                        verbose_name='Profissão do Fornecedor',
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        help_text='Digite o E-mail válido',
                        max_length=50,
                        verbose_name='E-mail de Contato',
                    ),
                ),
                (
                    'fixo',
                    models.CharField(
                        help_text='Número Fixo apenas número Sem traços ou parentes',
                        max_length=12,
                        verbose_name='Numero de fixo com o (DDD)',
                    ),
                ),
                (
                    'celular',
                    models.CharField(
                        blank=True,
                        help_text='Número do celular com o DDD Sem traços ou parentes',
                        max_length=11,
                        null=True,
                        verbose_name='Numero de celular com o (DDD)',
                    ),
                ),
                (
                    'what',
                    models.CharField(
                        blank=True,
                        help_text='Número de contato para o Whatzapp',
                        max_length=11,
                        null=True,
                        verbose_name='Contato do Whatzapp',
                    ),
                ),
                (
                    'situacao',
                    models.CharField(
                        choices=[('A', 'Ativo'), ('I', 'Inativo')],
                        default='A',
                        help_text='Escolha entre Ativo ou Inativo',
                        max_length=1,
                        verbose_name='Situação do Fornecedor',
                    ),
                ),
            ],
        ),
    ]

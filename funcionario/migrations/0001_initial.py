# Generated by Django 4.1.6 on 2023-03-06 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_departamento_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentosrh',
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
                    'descricao',
                    models.CharField(
                        help_text='Nome do documento completo',
                        max_length=100,
                        verbose_name='Nome do documento',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='HoraExtra_Funcionario',
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
                    'motivo',
                    models.CharField(
                        help_text='Nome do Motivo Hora extrar',
                        max_length=100,
                        verbose_name='Motivo Hora Extra',
                    ),
                ),
                (
                    'Logradouro',
                    models.CharField(
                        default='Rua',
                        help_text='Nome do Logradouro',
                        max_length=9,
                        verbose_name='Logradouro',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
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
                        help_text='Nome Completo do Cliente',
                        max_length=80,
                        verbose_name='Nome do cliente',
                    ),
                ),
                (
                    'Cpf',
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
                        help_text='Data de Nascimento do cliente',
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
                        help_text='Profissão Auto Declarada do Cliente',
                        max_length=80,
                        null=True,
                        verbose_name='Profissão do Cliente',
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
                        verbose_name='Situação do cliente',
                    ),
                ),
                (
                    'departamentos',
                    models.ManyToManyField(to='departamento.departamento'),
                ),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
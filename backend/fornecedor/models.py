from django.db import models

STATUS_SITUACAO = [
    ('A', 'Ativo'),
    ('I', 'Inativo'),
]


class Fornecedor(models.Model):
    nome = models.CharField(
        'Nome do Fornecedor',
        help_text='Nome Completo do Fornecedor',
        max_length=80,
    )
    CPF = models.CharField(
        'Número do CPF',
        help_text='Número do CPF, Sem traços ou pontos',
        max_length=15,
        blank=True,
    )

    CNPJ = models.CharField(
        'Número do CNPJ',
        help_text='Número do CNPJ, Sem traços ou pontos',
        max_length=20,
        blank=True,
    )
    rg = models.CharField(
        'RG', help_text='RG Sem traços ou pontos', max_length=15
    )
    datanascimento = models.DateField(
        'Data de nascimento',
        help_text='Data de Nascimento do Fornecedor',
        null=True,
        blank=True,
    )

    email = models.EmailField(
        'E-mail de Contato', help_text='Digite o E-mail válido', max_length=50
    )
    # uf = models.CharField(max_length=80)
    # cidade = models.CharField(max_length=80)
    # bairro = models.CharField(max_length=80)
    # logradouro = models.CharField(max_length=80)
    fixo = models.CharField(
        'Numero de fixo com o (DDD)',
        help_text='Número Fixo apenas número Sem traços ou parentes',
        max_length=12,
    )
    celular = models.CharField(
        'Numero de celular com o (DDD)',
        help_text='Número do celular com o DDD Sem traços ou parentes',
        max_length=11,
        blank=True,
        null=True,
    )
    what = models.CharField(
        'Contato do Whatzapp',
        help_text='Número de contato para o Whatzapp',
        max_length=11,
        blank=True,
        null=True,
    )
    situacao = models.CharField(
        'Situação do Fornecedor',
        help_text='Escolha entre Ativo ou Inativo',
        max_length=1,
        choices=STATUS_SITUACAO,
        null=False,
        blank=False,
        default='A',
    )

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome

from django.db import models


STATUS_SITUACAO = [
    ('A', 'Ativo'),
    ('I', 'Inativo'),
]

SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')]


class Cliente(models.Model):
    nome = models.CharField(
        'Nome do cliente', help_text='Nome Completo do Cliente', max_length=80, verbose_name='nome',
    )
    Cpf = models.CharField(
        'Número do CPF',
        help_text='Número do CPF, Sem traços ou pontos',
        max_length=15,
        verbose_name='CPF',
    )
    rg = models.CharField(
        'RG', help_text='RG Sem traços ou pontos',
        max_length=15, verbose_name='RG',
    )
    datanascimento = models.DateField(
        'Data de nascimento',
        help_text='Data de Nascimento do cliente',
        null=True,
        blank=True,
        verbose_name='Data de nascimento',
    )
    sexo = models.CharField(
        'Sexo',
        help_text='Escolha umas das opções',
        max_length=1,
        choices=SEXO_CHOICES,
        null=False,
        blank=False,
        default='M',
        verbose_name='sexo',

    )
    profissao = models.CharField(
        'Profissão do Cliente',
        help_text='Profissão Auto Declarada do Cliente',
        max_length=80,
        blank=True,
        null=True,
        verbose_name='profissao',
    )
    email = models.EmailField(
        'E-mail de Contato',
        help_text='Digite o E-mail válido',
        max_length=50,
        verbose_name='email',
    )
    # uf = models.CharField(max_length=80)
    # cidade = models.CharField(max_length=80)
    # bairro = models.CharField(max_length=80)
    # logradouro = models.CharField(max_length=80)
    fixo = models.CharField(
        'Numero de fixo com o (DDD)',
        help_text='Número Fixo apenas número Sem traços ou parentes',
        max_length=12,
        verbose_name='fixo',
    )
    celular = models.CharField(
        'Numero de celular com o (DDD)',
        help_text='Número do celular com o DDD Sem traços ou parentes',
        max_length=11,
        blank=True,
        null=True,
        verbose_name='celular',
    )
    what = models.CharField(
        'Contato do Whatzapp',
        help_text='Número de contato para o Whatzapp',
        max_length=11,
        blank=True,
        null=True,
        verbose_name='what',
    )
    situacao = models.CharField(
        'Situação do cliente',
        help_text='Escolha entre Ativo ou Inativo',
        max_length=1,
        choices=STATUS_SITUACAO,
        null=False,
        blank=False,
        default='A',
        verbose_name='situacao',
    )

    def __str__(self)
    return self.nome

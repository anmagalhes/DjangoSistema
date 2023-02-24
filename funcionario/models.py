from django.db import models
# from django.contrib.auth.models import User
from departamento.models import Departamento

STATUS_SITUACAO = [
    ('A', 'Ativo'),
    ('I', 'Inativo'),
]

SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')]


class Funcionario(models.Model):

    nome = models.CharField(
        'Nome do cliente', help_text='Nome Completo do Cliente', max_length=80
    )
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    Cpf = models.CharField(
        'Número do CPF',
        help_text='Número do CPF, Sem traços ou pontos',
        max_length=15
    )
    rg = models.CharField(
        'RG', help_text='RG Sem traços ou pontos',
        max_length=15
    )
    datanascimento = models.DateField(
        'Data de nascimento',
        help_text='Data de Nascimento do cliente',
        null=True,
        blank=True
    )
    sexo = models.CharField(
        'Sexo',
        help_text='Escolha umas das opções',
        max_length=1,
        choices=SEXO_CHOICES,
        null=False,
        blank=False,
        default='M'
    )
    profissao = models.CharField(
        'Profissão do Cliente',
        help_text='Profissão Auto Declarada do Cliente',
        max_length=80,
        blank=True,
        null=True
    )
    email = models.EmailField(
        'E-mail de Contato',
        help_text='Digite o E-mail válido',
        max_length=50
    )

    fixo = models.CharField(
        'Numero de fixo com o (DDD)',
        help_text='Número Fixo apenas número Sem traços ou parentes',
        max_length=12
    )
    celular = models.CharField(
        'Numero de celular com o (DDD)',
        help_text='Número do celular com o DDD Sem traços ou parentes',
        max_length=11,
        blank=True,
        null=True
    )
    what = models.CharField(
        'Contato do Whatzapp',
        help_text='Número de contato para o Whatzapp',
        max_length=11,
        blank=True,
        null=True
    )
    situacao = models.CharField(
        'Situação do cliente',
        help_text='Escolha entre Ativo ou Inativo',
        max_length=1,
        choices=STATUS_SITUACAO,
        null=False,
        blank=False,
        default='A'
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.Funcioanrio.nome


class Meta:
    verbose_name = 'funcionario'
    verbose_name_plural = 'funcionarios'

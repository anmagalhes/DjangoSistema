from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from backend.departamento.models import Departamento

STATUS_SITUACAO = [
    ('A', 'Ativo'),
    ('I', 'Inativo'),
]

SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')]


class Funcionario(models.Model):
    nome = models.CharField(
        'Nome do cliente', help_text='Nome Completo do Cliente', max_length=80
    )
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    cpf = models.CharField(
        'Número do CPF',
        help_text='Número do CPF, Sem traços ou pontos',
        max_length=15,
    )
    rg = models.CharField(
        'RG', help_text='RG Sem traços ou pontos', max_length=15
    )
    datanascimento = models.DateField(
        'Data de nascimento',
        help_text='Data de Nascimento do cliente',
        null=True,
        blank=True,
    )
    sexo = models.CharField(
        'Sexo',
        help_text='Escolha umas das opções',
        max_length=1,
        choices=SEXO_CHOICES,
        null=False,
        blank=False,
        default='M',
    )
    profissao = models.CharField(
        'Profissão do Cliente',
        help_text='Profissão Auto Declarada do Cliente',
        max_length=80,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        'E-mail de Contato', help_text='Digite o E-mail válido', max_length=50
    )

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
        'Situação do cliente',
        help_text='Escolha entre Ativo ou Inativo',
        max_length=1,
        choices=STATUS_SITUACAO,
        null=False,
        blank=False,
        default='A',
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'funcionário'
        verbose_name_plural = 'funcionários'

    def __str__(self):
        return self.nome

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('funcionario:funcionario_update', kwargs=kw)
        return None


class Documento(models.Model):
    descricao = models.CharField(
        'Nome do documento',
        help_text='Nome do documento completo',
        max_length=100,
    )

    class Meta:
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'

    def __str__(self):
        return self.descricao

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('funcionario:documento_update', kwargs=kw)
        return None


class HoraExtraFuncionario(models.Model):
    motivo = models.CharField(
        'Motivo Hora Extra',
        help_text='Nome do Motivo Hora extrar',
        max_length=100,
        null=False,
        blank=False,
    )
    logradouro = models.CharField(
        'Logradouro',
        help_text='Nome do Logradouro',
        max_length=9,
        null=False,
        blank=False,
        default='Rua',
    )

    class Meta:
        verbose_name = 'hora extra'
        verbose_name_plural = 'horas extra'

    def __str__(self):
        return self.motivo

    @property
    def update_url(self):
        if self.pk:
            kw = {'pk': self.pk}
            return reverse_lazy('funcionario:hora_extra_update', kwargs=kw)
        return None

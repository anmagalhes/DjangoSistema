from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("M","Masculino"),
        ("F","Feminino"),
        ("O","Outros"),
    )

    STATUS_SITUACAO = (
        ("A","Ativo"),
        ("I","Inativo"),
    )
    
    nome = models.CharField(
        'Nome do cliente',
        help_text='Nome Completo do Cliente',
        max_length=80)
    CPF = models.CharField(
        'Número do CPF',
        help_text='Número do CPF, Sem traços ou pontos',
        max_length=15)
    rg = models.CharField(
        'RG',
        help_text='RG Sem traços ou pontos',
        max_length=15)
    datanascimento = models.DateField(
        'Data de nascimento',
        help_text='Data de Nascimento do cliente',
        null=True,
        blank=True, 
    )
    sexo =  models.CharField(
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
        'E-mail de Contato',
        help_text='Digite o E-mail válido',
        max_length=50)
    #uf = models.CharField(max_length=80)
    #cidade = models.CharField(max_length=80)
    #bairro = models.CharField(max_length=80)
    #logradouro = models.CharField(max_length=80)
    fixo = models.CharField(
        'Numero de fixo com o (DDD)',
        help_text='Número Fixo apenas número Sem traços ou parentes',
        max_length=12)
    celular = models.CharField(
        'Numero de celular com o (DDD)',
        help_text='Número do celular com o DDD Sem traços ou parentes' ,
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
    situacao =  models.CharField(
        'Situação do cliente',
        help_text='Escolha entre Ativo ou Inativo',
        max_length=1,
        choices=STATUS_SITUACAO,
        null=False,
        blank=False, 
        default='A',
    )

    def __str__(self) -> str:
        return self.nome



  
    



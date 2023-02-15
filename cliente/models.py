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
    
    nome = models.CharField(max_length=80)
    numeroCPF = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)
    datanascimento = models.DateField(
        null=True,
        blank=True, 
    )
    sexo =  models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        null=False,
        blank=False, 
        default='M',
    )
    profissao = models.CharField(
        max_length=80,

    )
    email = models.EmailField(max_length=50)
    #uf = models.CharField(max_length=80)
    #cidade = models.CharField(max_length=80)
    #bairro = models.CharField(max_length=80)
    #logradouro = models.CharField(max_length=80)
    fixo = models.CharField(max_length=12)
    celular = models.CharField(max_length=11)
    what = models.CharField(max_length=11)
    situacao =  models.CharField(
        max_length=1,
        choices=STATUS_SITUACAO,
        null=False,
        blank=False, 
        default='A',
    )

    def __str__(self) -> str:
        return self.Cliente



  
    



from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("M","Masculino"),
        ("F","Feminino"),
        ("O","Outros"),
    )

    STATUSSITUACAO = (
        ("A","Ativo"),
        ("I","Desativado"),
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
        default='N',
    )
    profissao = models.CharField(
        max_length=80,
        default='N',
    )
    email = models.EmailField(max_length=50)
    #uf = models.CharField(max_length=80)
    #cidade = models.CharField(max_length=80)
    #bairro = models.CharField(max_length=80)
    #logradouro = models.CharField(max_length=80)
    dd = models.CharField(max_length=2)
    fixo = models.CharField(max_length=12)
    numero_celula = models.CharField(max_length=9)
    NumeroWhatazapp = models.CharField(max_length=9)
    situacao =  models.CharField(
        max_length=1,
        choices=STATUSSITUACAO,
        null=False,
        blank=False, 
        default='N',
    )

    def __str__(self) -> str:
        return self.Cliente



  
    



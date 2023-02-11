from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("M","Masculino"),
        ("F","Feminino"),
        ("O","Outros"),
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
    




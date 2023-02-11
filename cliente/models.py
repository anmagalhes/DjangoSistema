from django.db import models

class Sexo(models.Model):
    SEXO_CHOICES = (
        ("M","Masculino"),
        ("F","Feminino"),
        ("O","Outros"),
    ),

class Cliente(models.Model):
    nome = models.CharField(max_length=80)
    numeroCPF = models.CharField(max_length=15)
    rg = models.CharField(max_length=15)
    datanascimento = models.DateField(
        null=True,
        blank=True, 
    )



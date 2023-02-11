from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    STATUSPEDIDO_CHOICES = (
                ("A","Aprovado"),
                ("C","Criado"),
                ("E","Enviado"),
                ("F","Finalizado"),
                ("R","Reprovado"),
                ("p","Pendente"),
            )

    #usuario  = models.ForeignKey(User, on_delete=models.SET_NULL, null="true")
    total = models.FloatField(
        default=0
    )
    statuspedido =models.CharField(
        default="C",
        max_length=1,
        choices= STATUSPEDIDO_CHOICES,
        null=False,
    )
    
    def __str__(self) -> str:
        return self.nome
# Generated by Django 4.1.6 on 2023-02-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='statuspedido',
            field=models.CharField(
                choices=[
                    ('A', 'Aprovado'),
                    ('C', 'Criado'),
                    ('E', 'Enviado'),
                    ('F', 'Finalizado'),
                    ('R', 'Reprovado'),
                    ('p', 'Pendente'),
                ],
                default='C',
                max_length=1,
            ),
        ),
    ]

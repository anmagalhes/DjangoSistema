# Generated by Django 4.1.6 on 2023-02-12 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_remove_itempedido_pedido_itempedido_numeropedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itempedido',
            old_name='numeropedido',
            new_name='pedido',
        ),
    ]

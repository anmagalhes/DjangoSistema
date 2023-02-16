# Generated by Django 4.1.6 on 2023-02-12 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_itempedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='pedido',
        ),
        migrations.AddField(
            model_name='itempedido',
            name='numeropedido',
            field=models.ForeignKey(
                default='',
                on_delete=django.db.models.deletion.CASCADE,
                to='pedido.pedido',
            ),
            preserve_default=False,
        ),
    ]

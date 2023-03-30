# Generated by Django 4.1.6 on 2023-03-06 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'titulo',
                    models.CharField(
                        help_text='Nome Completo Catergoria',
                        max_length=40,
                        verbose_name='Nome Categoria',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'nome',
                    models.CharField(
                        help_text='Nome Completo Produto',
                        max_length=255,
                        verbose_name='Nome do Produto',
                    ),
                ),
                (
                    'quantidade',
                    models.FloatField(
                        default=0,
                        help_text='Quantidade produto, Sem traços ou pontos',
                        verbose_name='Quantidade do produto',
                    ),
                ),
                (
                    'categoria',
                    models.ForeignKey(
                        null='true',
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='estoque.categoria',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoEstoque',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'quantidade',
                    models.IntegerField(verbose_name='Quantidade de produto:'),
                ),
                (
                    'produto',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='estoque.produto',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Estoque',
                'verbose_name_plural': 'Estoques',
                'db_table': 'Estoque',
            },
        ),
    ]